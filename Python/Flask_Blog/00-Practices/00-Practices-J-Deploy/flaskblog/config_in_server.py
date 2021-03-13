import os

###################################################################
# Modify config.py in server side
import json
with open('/etc/config.json') as config_file:
    config = json.load(config_file)   # config is dictionary type
# change os.environ to config
###################################################################


class Config:
    # $ python
    # >>> import secrets
    # >>> secrets.token_hex(16)
    SECRET_KEY = config.get('SECRET_KEY')                              #'ada8419b155676bc78c2296aba9c7c7d'
    # /// represents the relative directory from the current file (flaskblog.py). 
    # that is, site.db has the same directory as this __init__.py
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')    #'sqlite:///site.db'

    # Config gmail server to send instruction how to reset password
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # environment variables 
    # Need to set these variables on Windows to your gmail user and password
    # ie.
    # > set EMAIL_USER xyz@gmail.com    (export in linux)
    # > set EMAIL_PASS password_to_xyz  (export in linux)
    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PASS')