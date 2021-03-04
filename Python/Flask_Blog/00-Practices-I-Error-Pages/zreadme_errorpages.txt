email: C@demo.com
password: password
email: zhjohn925@hotmail.com
password: 1234

- Create routes for error packages
- Create error pages template: 403.html, 404.html, 500.html
- Add to Blueprint in __init__.py

- Test website:
    1. 404 error:
    http://localhost:5000/no_such_page      

    2. 403 error:
    - log in an user
    - update post created by one other user
    http://localhost:5000/post/15/update

    
