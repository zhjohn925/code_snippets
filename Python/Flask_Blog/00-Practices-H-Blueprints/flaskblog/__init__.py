from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()   # Used to hash the password
login_manager = LoginManager()
mail = Mail()

# This (login_view) tells where is the login route located
login_manager.login_view = 'users.login'     # which is login() in 'users' blueprint
login_manager.login_message_category = 'info'  #add bootstrap class to make nice view for flash message


# create different applications per the given Config
def create_app(config_class=Config) :
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)  
    login_manager.init_app(app)
    mail.init_app(app)

    # import blueprints (users, posts, main)
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes  import main

    # register blueprints
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)  

    return app  