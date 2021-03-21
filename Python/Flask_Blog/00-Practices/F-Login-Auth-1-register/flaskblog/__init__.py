from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# $ python
# >>> import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'ada8419b155676bc78c2296aba9c7c7d'
# /// represents the relative directory from the current file (flaskblog.py). 
# that is, site.db has the same directory as this __init__.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)   # Used to hash the password

# import routes from flaskblog package
from flaskblog import routes