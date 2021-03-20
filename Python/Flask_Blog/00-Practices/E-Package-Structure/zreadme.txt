
1. python package is a directory with __init__.py

2. 
###################################################################
# Structure the Flask_Blog to use python package, 
# instead of python modules
###################################################################

$ tree /F
Folder PATH listing for volume DataDisk
Volume serial number is 8CB3-DF0B
D:.
│   run.py
│
└───flaskblog
    │   forms.py
    │   models.py
    │   routes.py
    │   site.db
    │   __init__.py
    │
    ├───static
    │       main.css
    │
    └───templates
            about.html
            home.html
            layout.html
            login.html
            register.html

3.
#############################################
# Generate database tables structure
#############################################

$ python
>>> from flaskblog import db
>>> from flaskblog.models import User, Post
>>> db.create_all()       #creates database structures. site.db is generated.
>>> User.query.all()
[]
>>> exit()

4.

