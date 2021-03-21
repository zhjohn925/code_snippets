1. update __init__.py by adding bcrypt, used to hash the password
          $ pip3 install flask-bcrypt
      look zreadme_bcrypt for details
      
2. update register() in routes.py to add user into the database, 
  and redirect to login page.
    - import db, bcrypt
    - add user and hashed password into database

3. test website 1
    $ python run.py
        http://127.0.0.1:5000/register
          register user: user1, email: user1@demo.com, pwd: 1234

    To verify the user being added:
    $ python
    >>> from flaskblog import db
    >>> from flaskblog.models import User
    >>> user = User.query.first()
    >>> user
        User('user1','user1@demo.com','default.jpg')
    >>> user.password      # get hashed password
    '$2b$12$nmigRg6eWScd8sAQoeckauz0Yb9WHM5/EdHa3RoGo4MIegELaqRTa'

4. test website 2, add same user: user1
          this can cause errors since user name should be unique as defined in User()
    $ python run.py
        http://127.0.0.1:5000/register
          register the same user: user1, pwd: 1234

5. add customized validation in RegistrationForm() in forms.py to prevent the above problem.
                from flaskblog.models import User
                def validate_username(self, username)
                def validate_email(self, email)

6. test website 3, add same user: user1,  and same email: user1@demo.com
        we should see the validation errors
    $ python run.py
        http://127.0.0.1:5000/register
          register the same user: user1, email: user1@demo.com

