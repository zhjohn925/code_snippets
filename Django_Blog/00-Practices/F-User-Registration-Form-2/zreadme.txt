
1. create our form that inherits Django UserCreationForm
    and add email field. 

    users/form.py
        from .form import UserRegisterForm
        class UserRegisterForm(UserCreationForm) :

2. update users/views.py by replacing 'UserCreationForm' 
    with 'UserRegisterForm'

3. test website (Now the register form with email)
        $ django_project> python manage.py runserver
        http://127.0.0.1:8000
        http://127.0.0.1:8000/register
            username: user6
            email:   user6@demo.com
            password: Temp!234

4. install crispy 
   (this third-party form is good for style, and easy to apply bootstrap)
   $ django_project> pip3 install django-crispy-forms

5. add crispy form in project settings.py

    --  INSTALLED_APPS = [
            'blog.apps.BlogConfig',
            'users.apps.UsersConfig',
            'crispy_forms',

    --  # specify crispy forms apply for bootstrap css framework
        CRISPY_TEMPLATE_PACK = 'bootstrap4'

6. add crispy into register template (users/register.html)
       <!-- load crispy_forms_tags allows us to use 
                         crispy filter to the form --> 
        {% load crispy_forms_tags %}

       <!-- apply crispy filter | -->
        {{ form | crispy }}

7. test website (Now we can see better form view)
        $ django_project> python manage.py runserver
        http://127.0.0.1:8000
        http://127.0.0.1:8000/register

    -- Use Inspect to view source, we can see bootstrap css are added
    for free.
    -- test validations
    ie. register the existing user, mismatch password
    

