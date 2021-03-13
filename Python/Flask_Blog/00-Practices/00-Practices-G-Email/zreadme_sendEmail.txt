email: C@demo.com
password: password
email: zhjohn925@hotmail.com
password: 1234

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
In order to send email from gmail, need to
1. enable access for less secure apps in gmail account
2. on Windows environment variables
   > set EMAIL_USER=zhjohn925@gmail.com
   > set EMAIL_PASS=<your gmail pwd>
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Send email: 
To Reset password:

0. install flask-mail
   $ pip3 install flask-mail

1. look at the token (payload) demo below.
2. Update User() in models.py with 
     from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
     get_reset_token()
     verify_reset_token()
3. Add RequestResetForm(), and ResetPasswordForm() in forms.py
4. create reset_request() route in route.py, send_reset_email()
5. create reset_request.html template
6. create reset_token route in route.py
7. add MAIL server in __init__.py
8. add mail, send_reset_email() in route.py
9. update reset_token() route in route.py
10. update the link to "Forgot Password" in login.html








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
