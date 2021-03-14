
1. Install flask-wtf
    $ pip3 install flask-wtf

2. create forms.py    
    - class RegistrationForm (FlaskForm) :
    - class LoginForm (FlaskForm) :

    In order to use form, we need to set security key 
    for this application

3. set security key in flaskblog.py

        # $ python
        # >>> import secrets
        # >>> secrets.token_hex(16)
        app.config['SECRET_KEY'] = 'ada8419b155676bc78c2296aba9c7c7d'

4. add register() and login() routes in flaskblog.py
        
        from forms import RegistrationForm, LoginForm

        @app.route("/register")
        def register():
            ::::::

        @app.route("/login")
        def login():
            ::::::

5. create register.html template 

    <!-- leave action empty, so that the page stays at the same route
            after the "post" request -->
    <form action="" method="post">

    {{ form.hidden_tag() }} adds csrf tokens in the form for protection.

    some bootstrap css ie. 
            .label(class="form-control-label")

    form.username, form.email and etc are field names which are 
            defined in RegistrationForm class in form.py

6. create login.html template (copy register.html and do changes)

7. Test website
   $ python flaskblog.py  
        http://127.0.0.1:5000/register

    If you try to submit the form, you may see the error: 
    "Method Not Allowed", since the 'POST' method is not defined 
    in the register route. 

8. Add the method in register() and login() routes

    @app.route("/register", methods=['GET', 'POST'])
    @app.route("/login", methods=['GET', 'POST'])

9. Test website
   $ python flaskblog.py  
        http://127.0.0.1:5000/register