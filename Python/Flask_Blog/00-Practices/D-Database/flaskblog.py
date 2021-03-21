from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# $ python
# >>> import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'ada8419b155676bc78c2296aba9c7c7d'
# SQLite is a database engine
# It is great for prototyping an application before moving 
# to a larger database such as MySQL or Postgres.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site2.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # --posts is not a column, but a relationship running a query 
    #   in background to collect all the posts by this user
    # --lazy=true, SQLALCHEMY loads the data as necessary in one go
    # --backref is a simple way to declare a new property on the Post class. 
    #   You can then use post.author to get to the user who writes the post.
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # Use a foreign key that references the primary key of User table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


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


# apply route decorator
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # once submit successfully, flash message shows in the placehold in layout.html
    # flash message is one time only, it disappear after refresh web browser
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data } !', 'success')
        # 'home' is function of home() route
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() :
        if form.email.data == 'admin@demo.com' and form.password.data == '1234':
            flash('You have been logged in !', 'success')
            return redirect(url_for('home'))
        else :
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__' :
    app.run(debug=True)