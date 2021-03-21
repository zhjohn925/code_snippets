
1. create logout() route in routes.py
      -- import logout_user
      -- def logout()

2. update the layout.html template to add 'logout' navbar
      Use Jinja2
      ie. 
      {% if current_user.is_authenticated  %}
            <a class="nav-item nav-link" href="{{ url_for('logout') }}">Logout</a>

