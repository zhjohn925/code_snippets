
1. Update account.html template with account.html in snippets

2. replace username, email with current_user

3. add static\profile_pics\default.jpg

4. add img_file in account() route in routes.py 
   pass img_file to account.html template

5. Use image_file in account.html template

6. test website
      http://127.0.0.1:5000/
      http://127.0.0.1:5000/account

7. Create UpdateAccountForm() in forms.py
      - import current_user
      - change validate_username and validate_email only when the new username and 
            email are different from current_user
      
8. Apply UpdateAccountForm in account() route in routes.py
      - import UpdateAccountForm
      - form = UpdateAccountForm()
      - pass form into account.html template

9. Update account.html template with form view
      - copy form in register.html and modify

10. test website
      http://127.0.0.1:5000/
      http://127.0.0.1:5000/account

      try to update account username and email, and submit
      you will hit the errors. ie. 
            Method Not Allowed
      it is because there is no "methods=['GET', 'POST']" in account() route