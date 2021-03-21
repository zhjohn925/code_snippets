from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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
    return render_template('home.html', posts=posts)

# http://localhost:5000/about
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # once submit successfully, flash message shows in the placehold in layout.html
    # flash message is one time only, it disappear after refresh web browser
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data=='password' :
            flash('You have been logged in', 'success')
            # 'home' is function of home() above
            return redirect(url_for('home'))
        else :
            flash('Login failed. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
