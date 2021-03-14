
1. Update layout template with bootstrap 4 css framework

    <!-- https://getbootstrap.com/docs/4.0/getting-started/introduction/ -->
    <!-- look for 'Starter template', and copy css and javascript -->

2. Add div.container (bootstrap css) in templates/layout.html
        <div class="container">
            {% block content %}{% endblock %} 
        </div>

3. Test website
   $ python flaskblog.py  
   (Must restart the web server to load new css, 
    or CTRL+SHIFT+R to force web browser to reload css)
        http://127.0.0.1:5000/home
        http://127.0.0.1:5000/about
    Now we can see some margin in the views due to bootstrap css