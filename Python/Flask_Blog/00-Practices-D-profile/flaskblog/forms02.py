from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

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

    # The validate functions Must follow the format in order to get validation
    #      def validate_field(self, field) : 
    # the fields have username, email and etc in above.
    # The below makes sure no same username and email is registered. 

    def validate_username(self, username) :
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email) :
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm (FlaskForm) :
    email    = StringField('Email',    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # This (remember) allows users to stay login for certain time 
    # after web browser closes by using security cookies. 
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

# Copy RegistrationForm to modify
class UpdateAccountForm (FlaskForm) :
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email    = StringField('Email',    validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    # The validate functions Must follow the format in order to get validation
    #      def validate_field(self, field) : 
    # the fields have username, email and etc in above.
    # The below makes sure no same username and email is registered. 

    # validate only when username is not current_user's username
    def validate_username(self, username) :
        if username.data != current_user.username :
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    # validate only when email is not current_user's email          
    def validate_email(self, email) :
        if email.data != current_user.email :
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

