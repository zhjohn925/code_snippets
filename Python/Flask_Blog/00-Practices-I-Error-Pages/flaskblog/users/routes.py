from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email


users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
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
        return redirect(url_for('users.login'))
    return render_template('register12_error.html', title='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data) :
            login_user(user, remember=form.remember.data)
            # request.args is dictionary type
            next_page = request.args.get('next')
            # 'home' is function of home() above
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else :
            flash('Login failed. Please check email and password.', 'danger')
    return render_template('login13.html', title='Login', form=form)


@users.route("/logout")
def logout() :
    logout_user()
    return redirect(url_for('main.home'))



# login_required decorator makes sure to access the page only
# when the user log in
@users.route("/account", methods=['GET', 'POST'])
@login_required
def account() :
    # this form is for user to update the profile
    form = UpdateAccountForm()
    if form.validate_on_submit() :
        if form.picture.data :
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        # think of current_user is reference to the User in database
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET' :
        # populate the username and email so that
        # the new username and email can be viewed right after 
        # update form is submitted
        form.username.data = current_user.username
        form.email.data = current_user.email
    # user.image_file is defined in User() in models.py from database
    image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
    return render_template('account04.html', title='Account', image_file=image_file, form=form)


@users.route("/user/<string:username>")
def user_posts(username) :
    page = request.args.get('page', 1, type=int)
    # first_or_404: first user or give 404 if no user is found
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
                    .order_by(Post.date_posted.desc())\
                    .paginate(page=page, per_page=2)
    return render_template('user_posts.html', posts=posts, user=user)


# route the form to send instruction email to request password reset
# when forgot the password
@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request() :
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)



# route with the form to set new password (the URL link is from email)
@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token) :
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    # the token comes with user id. if the user id is valid,
    # the valid user is returned    
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # hash the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))    
    return render_template('reset_token.html', title='Reset Password', form=form)