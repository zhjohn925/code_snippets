from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db, login_manager, app
from flask_login import UserMixin

### !!! Generate database tables structure first 
### !!! by following zreadme_package.txt

@login_manager.user_loader
def load_user(user_id) :
    return User.query.get(int(user_id))


# defines User table structure in database
class User(db.Model, UserMixin) :
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
    # --posts is not a column, but a relationship running a query 
    #   in background to collect all the posts by this user
    # --lazy=true, SQLALCHEMY loads the data as necessary in one go
    # --backref is a simple way to declare a new property on the Post class. 
    #   You can then use post.author to get to the user who writes the post.
    posts = db.relationship('Post', backref='author', lazy=True)

    # token expires after 1800 seconds (30 min)
    # {'user_id': self.id} as payload
    def get_reset_token(self, expires_sec=1800) :
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    # @staticmethod decorator tells python this member function
    # does not need self as parameter 
    # s.loads(token) gets payload which is {'user_id': self.id}
    # So, s.loads(token)['user_id'] returns self.id
    @staticmethod
    def verify_reset_token(token) :
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

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
    # Use a foreign key that references the primary key of User table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # function to print this class (Post)
    def __repr__(self) :
        return f"Post('{self.title}','{self.date_posted}')"
