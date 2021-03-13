
1. create 'users' app
        $ django_project> python manage.py startapp users

2. add users config in django_project/settings.py
        INSTALLED_APPS = [
                'blog.apps.BlogConfig',
                'users.apps.UsersConfig',

    we can find UsersConfig in users/apps.py   

3. create register() route in users/views.py
        Django provides UserCreationForm for user register form
        save form into database
        add flash message (display only one time, disappear after refresh web browser)

4. create register.html template in users/templates/users 
         {{ form }} can be also replaced by
         {{ form.as_p }}

5. add flash message view in blog/templates/blog/base.html
   right before {% block content %}   
       <div class="alert alert-{{message.tags}}">{{ message }}</div>
    
6. add register path (url) in django_project/urls.py

     path('register/', user_views.register, name='register'),

7. test website
        $ django_project> python manage.py runserver
        http://127.0.0.1:8000
        http://127.0.0.1:8000/register
        Sign up two users:  
        (Use uncommon password. otherwise, sign up errors can occur)
        username: user2,  pwd: Temp!234  
        username: user3,  pwd: Temp!234
        
        http://127.0.0.1:8000/admin
        Log in with super user (created previously)
        user: user1
        pwd:  temp1234
        We can see two users were created in admin page. but no email information
        since Django UserCreationForm has no email field.  
        Therefore, we need to create our own form, and inherit Django UserCreationForm.
         
