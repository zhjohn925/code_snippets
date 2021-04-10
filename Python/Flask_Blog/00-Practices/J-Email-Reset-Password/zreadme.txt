
1. look at the token (payload) demo below.

    $ python
    >>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer 
    >>> s = Serializer('secret', 30)     # token expires in 30 seconds
    >>> token = s.dumps({'user_id': 1}).decode('utf-8')   # {'user_id': 1} as payload
    >>> token
    'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxNDY1NTYwMiwiZXhwIjoxNjE0NjU1NjMyfQ.eyJ1c2VyX2lkIjoxfQ.7R8LOCtZJ83OhB6er_0eGf7UxsL3HPI5y0DN2W2cdyXQoiwXDBRgeSSshQCZVlFnlQbbHzajTjSwKQCuE6-ZzA'
    >>> s.loads(token)     # this must be done in 30 seconds to get payload. OR it fails due to token expires.
    {'user_id': 1}  # payload
    >>> s.loads(token)   # it fails if wait for more than 30 seconds
    itsdangerous.exc.SignatureExpired: Signature expired


2. install flask-mail
   $ pip3 install flask-mail

3. Update User() in models.py with 
     from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
     from flaskblog import db, login_manager, app
     get_reset_token()
     verify_reset_token()

4. Add RequestResetForm(), and ResetPasswordForm() in forms.py

5. create reset_request() route in route.py

    Send email with the link to reset the password once the user requests 
    password reset. 
    The token in the link comes with {'user_id': self.id} as payload.

        - from flaskblog.forms import (RegistrationForm, LoginForm, UpdateAccountForm, 
                             PostForm, RequestResetForm, ResetPasswordForm)
        - from flaskblog import app, db, bcrypt, mail
                    mail is declared in __init__ as below
        - from flask_mail import Message
        - send_reset_email()

    Example in email:
        To reset your password, visit the following link:
        http://127.0.0.1:5000/reset_password/eyJhb...rTSAYww

6. create reset_request.html template
        view to request password reset. 

7. create reset_token route in route.py
    The link in the email is routed to reset_token(). 
    The token in the link comes with {'user_id': self.id} as payload to query 
        the user to update the new password. 

8. create reset_token.html template
        view to update the new password.

9. add MAIL server in __init__.py
        import os
        from flask_mail import Mail

        # Config gmail server to send instruction how to reset password
        app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
        app.config['MAIL_PORT'] = 587
        app.config['MAIL_USE_TLS'] = True

        # environment variables 
        # Need to set these variables on Windows to your gmail user and password
        # ie.
        # > set EMAIL_USER xyz@gmail.com    (use 'export' in linux)
        # > set EMAIL_PASS password_to_xyz  (use 'export' in linux)
        app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
        app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
        mail = Mail(app)

10. update the link to "Forgot Password" in login.html

        <small class="text-muted ml-2">
            <a href="{{ url_for('reset_request') }}">Forgot password ?</a>
        </small>


11. test website
    http://127.0.0.1:5000/login
        try to reset password

    - Register an user with real email 
        user: zhjohn925
        email: zhjohn925@hotmail.com
        password: 1234
    - The email with the link to reset password is sent via GMAIL
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        In order to send email from gmail, need to
        1. enable access for less secure apps in gmail account
        2. on Windows environment variables (Use 'export' in linux)
            > set EMAIL_USER=zhjohn925@gmail.com
            > set EMAIL_PASS=<your gmail pwd>
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    - http://127.0.0.1:5000/login
        - click "Forgot the password" to reset password
        - the link to reset password is sent to hotmail 
        - click the link to set new password
        
        







