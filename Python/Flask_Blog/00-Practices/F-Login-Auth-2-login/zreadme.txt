
1. $ pip3 install flask-login 

2. import LoginManager in __init__.py
      now we are ready to use LoginManager in the app

3. add login_manager in models.py
      -- def load_user(user_id) 
      -- import UserMixin
          Class UserMixin provides these properties and methods
          -- is_authenticated
          -- is_active
          -- is_anonymous
          -- get_id()
      -- User inherits UserMixin

4. work on login() route in routes.py
      -- remove the previous hard-coded user and password.
         change to get user and password from the database   
      ie. 
          user = User.query.filter_by(email=form.email.data).first()
          if user and bcrypt.check_password_hash(user.password, form.password.data) :
            login_user(user, remember=form.remember.data) 

5. test website (try correct and wrong password)
      http://127.0.0.1:5000/register    # if no user is registered
      http://127.0.0.1:5000/login
      user: user1@demo.com
      pwd:  1234

            Note: we can still see 'Login' navbar after login the account
                  this is not normal

6. apply for 'current_user' in flask_login
      -- import current_user in routes.py
      -- add current_user in register() route
      -- add current_user in login() route
            ie. 
            if current_user.is_authenticated:
                return redirect(url_for('home'))

7. test website (after login, we should see home page)
      http://127.0.0.1:5000/register   
      http://127.0.0.1:5000/login
  
      But we do not want to see 'register' and 'login' navbar after login 






