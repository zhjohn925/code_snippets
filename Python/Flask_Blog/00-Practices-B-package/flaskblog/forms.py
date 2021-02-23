from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# $ pip3 install flask_wtf
# $ pip3 install email_validator

# This module is imported in flaskblog.py to create forms

class RegistrationForm (FlaskForm) :
    #                      'Username' in html      pass objects in validators
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email    = StringField('Email',    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

class LoginForm (FlaskForm) :
    email    = StringField('Email',    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # This (remember) allows users to stay login for certain time 
    # after web browser closes by using security cookies. 
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')