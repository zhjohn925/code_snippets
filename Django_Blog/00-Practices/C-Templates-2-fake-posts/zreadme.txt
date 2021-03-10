
1. add fake 'posts' in blog/views.py to demo 
    how to pass python variables into html templates

2. add 'context = { 'posts': posts }' in home() in blog/views.py

3. - update templates/blog/home.html to view the posts
   - Add title in templates/blog/home.html
   - Add title in templates/blog/about.html

4. test website
    django_project> python manage.py runserver
    http://127.0.0.1:8000/           
    http://127.0.0.1:8000/about  

