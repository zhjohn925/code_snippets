from datetime import datetime
from flaskblog import db

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
