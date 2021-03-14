
1. template inherit. 
   create layout template (layout.html) in templates

        <!-- placeholder for unique contents in each page -->
        {% block content %}{% endblock %} 

2. update home and about templates to inherit layout template

        {% extends "layout.html" %}
        {% block content %}
            ::::::
        {% endblock content %}

3. Test website
   $ python flaskblog.py  (if web server is not UP)
        http://127.0.0.1:5000/home
        http://127.0.0.1:5000/about
    Now we can see same views with layout template inherited