
1. create account() route in routes.py
      # login_required decorator makes sure to access the page only
      # when the user log in
            @app.route("/account")
            @login_required

2. create account.html template in /templates
      -- just view {{ current_user.username }} for now

3. add account navbar in /templates/layout.html     
      <a class="nav-item nav-link" href="{{ url_for('logout') }}">Account</a>

4. test website
      - after log in,  it shows username
      http://127.0.0.1:5000/account

      - after logout, it shows "unauthorized" message, to fix this, do step 5
            we really want to route it to login page
      http://127.0.0.1:5000/account

5. add login_view in __init__.py.   
      'login' is function name of route in routes.py
              login_manager.login_view = 'login'

6. test website
      - after log in,  it shows username
      http://127.0.0.1:5000/account

      - after logout, it shows login page
      http://127.0.0.1:5000/account

7. add bootstrap category 'info' for login message in __init__.py
      login_manager.login_message_category = 'info'

8. test website
      we will see flash message looks better now
           "Please log in to access this page."
      - after logout, it shows login page
      http://127.0.0.1:5000/account

      HERE, we can see it redirect to login page as expected.  but after login,
      it is re-direct to home page. while the user asks for account page. 
      we can fix this in step 9

9. Update routes.py 
      - import request object
      - add in login() route
            next_page = request.args.get('next')

10. test website
      - after logout, it shows login page
      http://127.0.0.1:5000/account

      - after login, it shows account page 
