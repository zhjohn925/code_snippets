
1. create blog/templates/blog/base.html

2. modify home.html, about.html to extend (inherit) base.html
    by adding stuff in {% block content %} {% endblock %}

3. test website
    django_project> python manage.py runserver (if server not UP)
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/about

