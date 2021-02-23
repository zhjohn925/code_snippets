from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

# $ pip3 install flask_sqlalchemy
# Then we need to specify URI, the location where is the database stored
# Then declare 'db' 
# Then define database structure ie. User table, Post table and etc
# Look at zreadme_db.txt to understand how to operate the db

app = Flask(__name__)

# $ python
# >>> import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'ada8419b155676bc78c2296aba9c7c7d'
# /// represents the relative directory from the current file (flaskblog.py). 
# that is, site.db has the same directory as flaskblog.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# defines User table structure in database
class User(db.Model) :
    # primary_key specifies unique id
    id = db.Column(db.Integer, primary_key=True)
    # max 20 characters, unique, and required
    username = db.Column(db.String(20), unique=True, nullable=False)
    # max 120 characters, unique, and required
    email = db.Column(db.String(120), unique=True, nullable=False)
    # profile image
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # password (be hashed)
    password = db.Column(db.String(60), nullable=False)
    # This is not a column, but build relationship between post and author
    # 'Post' class being passed
    # backref 'author' is reference to the user by post.author
    posts = db.relationship('Post', backref='author', lazy=True)

    # function to print this class (User)
    def __repr__(self) :
        return f"User('{self.username}','{self.email}','{self.image_file}')"

# defines Post table structure in database
class Post(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # type of DateTime, the current time as default (utcnow)
    # The default is passed as the function name of utcnow. Do not use 
    # utcnow(), which can invoke the function right away. 
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # point to user who creates this post
    # 'user' in 'user.id' is reference to an user in the User table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # function to print this class (Post)
    def __repr__(self) :
        return f"Post('{self.title}','{self.date_posted}')"


# add variables, use Jinja2 to pass into html
posts = [
    {
        'author': 'Corey Schafer', 'title': 'Blog Post 1',
        'content': 'First post content', 'date_posted': 'April 20, 2018'
    },
        {
        'author': 'Jane Doe', 'title': 'Blog Post 2',
        'content': 'Second post content', 'date_posted': 'April 21, 2018'
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
    form = RegistrationForm()
    # once submit successfully, flash message shows in the placehold in layout.html
    # flash message is one time only, it disappear after refresh web browser
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data } !', 'success')
        # 'home' is function of home() above
        return redirect(url_for('home'))
    return render_template('register12_error.html', title='Register', form=form)

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
    return render_template('login13.html', title='Login', form=form)

if __name__ == '__main__' :
    app.run(debug=True)