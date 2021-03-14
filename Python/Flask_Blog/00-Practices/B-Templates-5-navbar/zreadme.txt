
1. Create navbar by
    Copy snippets/navigation.html into templates/layout.html

2. Create main section by 
    Copy snippets/main.html into templates/layout.html
    Note the {% block content %}{% endblock %} is moved to main section

    <!-- bootstrap css divides 8 grids for block content, 
        and 4 grids for side bar -->
            <div class="col-md-8">
                {% block content %}{% endblock %}
            </div>
            <div class="col-md-4">
                <!-- side bar -->
            </div>

3. add our own css style main.css
    Create static directory, copy snippets/main.css into static directory

4. update templates/layout.html to apply main.css style
        ( and, import url_for in flaskblog.py)

    href="{{ url_for('static', filename='main.css') }}

    The 'margin-top' also adds space between navbar and main section. 
    otherwise, both are overlapped in the view
        body {
            :::::::
            margin-top: 5rem;
        }

5. Test website
   $ python flaskblog.py  
        http://127.0.0.1:5000/home
        http://127.0.0.1:5000/about
    Now we can see navbar and side bar in the views

6. Update posts section in templates/home.html by 
    copy snippets/article.html

        {% for post in posts %}
        <article class="media content-section">
            :::::::
        </article>
        {% endfor %}

7. Test website
   $ python flaskblog.py  
        http://127.0.0.1:5000/home
    Now we can see better view of posts 