from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms04 import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import os, secrets
from PIL import Image

# forms.py in flaskblog package
# models.py in flaskblog package

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


# http://localhost:5000/
@app.route("/")
@app.route("/home")
def home():
    return render_template('home11_flash.html', posts=posts)

# http://localhost:5000/about
@app.route("/about")
def about():
    return render_template('about11_flash.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    # once submit successfully, flash message shows in the placehold in layout.html
    # flash message is one time only, it disappear after refresh web browser
    if form.validate_on_submit():
        # hash the password
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        # 'home' is function of home() above
        return redirect(url_for('login'))
    return render_template('register12_error.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data) :
            login_user(user, remember=form.remember.data)
            # request.args is dictionary type
            next_page = request.args.get('next')
            # 'home' is function of home() above
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else :
            flash('Login failed. Please check email and password.', 'danger')
    return render_template('login13.html', title='Login', form=form)


@app.route("/logout")
def logout() :
    logout_user()
    return redirect(url_for('home'))

# save uploaded image to the specified path
def save_picture(form_picture) :
    random_hex = secrets.token_hex(8)
    # underscore (_) ignoring the value
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    # define the path to store profile image
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
   
    # save the uploaded image into the specified path

    # do not want to save the original uploaded image, which can be very large
    #form_picture.save(picture_path)

    #resize the image before store
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# login_required decorator makes sure to access the page only
# when the user log in
@app.route("/account", methods=['GET', 'POST'])
@login_required
def account() :
    # this form is for user to update the profile
    form = UpdateAccountForm()
    if form.validate_on_submit() :
        if form.picture.data :
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        # think of current_user is reference to the user in database
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET' :
        # populate the username and email so that
        # the new username and email can be viewed right after 
        # update form is submitted
        form.username.data = current_user.username
        form.email.data = current_user.email
    # user.image_file is defined in User() in models.py from database
    image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
    return render_template('account04.html', title='Account', image_file=image_file, form=form)