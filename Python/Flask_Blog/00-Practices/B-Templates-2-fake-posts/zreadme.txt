
1. create posts variable in flaskblog.py

2. pass 'posts' into home template in flaskblog.py

    def home():
    return render_template('home.html', posts=posts)

3. update templates/home.html to view the posts by using Jinja2
        {% for post in posts %}
            ::::::
        {% endfor %}

4. Test website
   $ python flaskblog.py
        http://127.0.0.1:5000/home

5. pass 'title' into about template in flaskblog.py

    def about():
        return render_template('about.html', title='About')

6. update <title> tag in home and about template to view the web page title

    {% if title %}
        ::::::
    {% endif %}  

7. Test website
   $ python flaskblog.py  (if web server is not UP)
        http://127.0.0.1:5000/home
        http://127.0.0.1:5000/about
    Now we can see web page title  