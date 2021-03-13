from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# add email field into the form

class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField()

    class Meta:
        # specify this form map to User in the database
        model = User
        # define fields in the register form template
        fields = ['username', 'email', 'password1', 'password2']