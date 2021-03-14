
1. import flash in flaskblog.py

2. create flash message after form is validated in register() route
        in flaskblog.py

    flash(f'Account created for { form.username.data } !', 'success')

3. add view for flash message in templates/layout.html

    <!-- with_categories=true so that the function also returns the status
        categories ie. success, warn, info and etc for bootstrap css style -->
    {% with messages = get_flashed_messages(with_categories=true) %}

4. Test website
   $ python flaskblog.py  
        http://127.0.0.1:5000/register

    After submit the form, we should see the flash message on home view.
    Note, the flash message is one time only. it disappears after reload 
    the web page.

    

