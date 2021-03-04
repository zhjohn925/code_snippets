import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)   # Used to hash the password
login_manager = LoginManager(app)
# This (login_view) tells where is the login route located
login_manager.login_view = 'login'     # which is login() in routes.py
login_manager.login_message_category = 'info'  #add bootstrap class to make nice view for flash message

mail = Mail(app)

# import blueprints (users, posts, main)
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes  import main

# register blueprints
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)