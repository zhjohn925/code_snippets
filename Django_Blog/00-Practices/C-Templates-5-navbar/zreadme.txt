
1. copy navbar template view (navigation.html) in snippets 
        into blog/templates/blog/base.html

2. copy main section view (main.html) in snippets to 
        replace {% block content %} in blog/templates/blog/base.html
        - main section also comes with side bar 

3. copy main.css in snippets to blog/static/blog

4. add main.css into base template (blog/templates/blog/base.html)
        {% load static %}
        <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

5. rewrite posts section in blog/templates/blog/home.html
        by adding bootstrap css (copy article.html in snippets)

6. change hard-coded href links in navbar (base.html) to django url path  
        (the path name defined in blog/urls.py)
        '/'      ---->  {% url 'blog-home' %}
        '/about' ---->  {% url 'blog-about' %}
        This way can be easy to change the routes just in one place (urls.py).
        Keep the code easy to maintain.


7. test website
    Must restart the webserver to load new css:
        django_project> python manage.py runserver
        http://127.0.0.1:8000/
        http://127.0.0.1:8000/about




