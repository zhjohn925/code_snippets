- update __init__.py by adding bcrypt, used to hash the password
          $ pip3 install flask-bcrypt
      look zreadme_bcrypt for details
      
- update register() in routes.py to add user into the database, 
  and redirect to login page.
  To verify the user being added:
  $ python
  >>> from flaskblog import db
  >>> from flaskblog.models import User
  >>> user = User.query.first()
  >>> user
  User('cinindyz','C@demo.com','default.jpg')
  >>> user.password      # get hashed password
  '$2b$12$nmigRg6eWScd8sAQoeckauz0Yb9WHM5/EdHa3RoGo4MIegELaqRTa'
- update RegistrationForm in forms.py to validate the existing username 
  and email.
- install flask-login
  $ pip3 install flask-login
- update __init__.py by adding LoginManager
- add load_user(), UserMixin in models.py
- update login() in routes.py to compare user and password in database
- add current_user in routes.py to redirect to home page 
  when click login and register
- add logout route in routes.py
- add logout navbar in layout.html
- create account route in routes.py, which is for the page when user log in 
- create account.html template, and add Account navbar in layout.html
- add login_required in routes.py, which allows user to access account.html 
  only when the user log in
- add next_page in login() in routes.py
  this achieves the scenario if access to localhost/account when the 
  user not logged in,  the next_page would hold account.html to view after
  the user log in. And, another scenario if access to localhost/login when 
  the user not logged in, the next_page would hold None to view home page 
  after the user log in.
 




########################################
# encrypt the password
########################################

# Note: password is stored as hash in database
#

$ pip3 install flask-bcrypt

$ python
>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()
>>> bcrypt.generate_password_hash('testing')
b'$2b$12$4si67CpPMi4rA18nN87oMezHRxvfzngEwmbneJ0Cq01uwK5p42qZG'
>>> bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$FcFZ7DBE4p840HazcDxTrusHMN0THuHTolLGJd1DV6wCANuY6HC02'
>>> bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$.po50VU/tuNhNQXz/A7ezOkFEtC6VEnigbKwk1Bznaxgs4sixaMBO'

# b means byte - default hash format
# utf-8: hash in string format
# The results are different each time bcrypt.generate_password_hash('testing')
# To verify the correct password by using bcrypt.check_password_hash()

>>> correct_pwd = 'testing'
>>> wrong_pwd = 'test1ng'
>>> hashed_pwd = bcrypt.generate_password_hash(correct_pwd).decode('utf-8')
>>> hashed_pwd
'$2b$12$IjHyIM3y5kT676AuNzKFZeVrq5c5/94.RsnVDbPZke/Vt4iUvw2WW'
>>> bcrypt.check_password_hash(hashed_pwd, wrong_pwd)
False
>>> bcrypt.check_password_hash(hashed_pwd, correct_pwd)
True

