
1. add form validation errors in register.html and login.html template

        {% if form.username.errors %}
            ::::::
        {% else %} 
            ::::::
        {% endif %} 

    Note: in order to show the above errors in the view, 
        flaskblog.py need to call 'form.validate_on_submit()'
        in home(), login() route 


2. Test website
   $ python flaskblog.py  
        http://127.0.0.1:5000/register

    Make some invalid fields in the form, then submit to show the errors

3. add validate submit check in login() route in flaskblog.py
    
    - Input some invalid email to test the error message

    - Make up a fake username and password to login 
        (do not have database yet) 
    - flash message is generated for login ok or fails

4. Test website
   $ python flaskblog.py  
        http://127.0.0.1:5000/login

5. use usr_for() to route pages in templates/layout.html 
   This can have some benefit in routing

