
1. Add "methods=['GET', 'POST']" in account() route 

2. test website
      http://127.0.0.1:5000/
      http://127.0.0.1:5000/account

      Try to update username or email, and submit
      You will see nothing happens.  
      it is because the update does not go to database yet

3. Store form data into database in account() route in routes.py
      - if form.validate_on_submit() :
            # think of current_user is reference to the user in database
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
      - add flash message
      - redirect to account view (This is Must !)
                  return redirect(url_for('account'))
            We are already in account template/view, why it needs this redirect() ?
            It is because the web browser (client) sends "POST" request, then 
            redirect() forces the client to send "GET" request to update the view.
            if skip redirect(), the route will do render_template(). It sends "POST"
            request again. 
            Sometimes, the web browser can give the warnings due to this problem. 

4. Update account() route in routes.py after the form is submitted
      to populate the update in the template/view. that is,  the new username 
      and email can be viewed right after update form is submitted  

            elif request.method == 'GET' :
                  form.username.data = current_user.username
                  form.email.data = current_user.email

5. test website
      http://127.0.0.1:5000/
      http://127.0.0.1:5000/register
      Before doing this, register a new user: user2
      http://127.0.0.1:5000/account
      Then log in user1, and try to update user1 with user2, we should 
      see the errors. ie. 
            "That username is taken. Please choose a different one."
      



