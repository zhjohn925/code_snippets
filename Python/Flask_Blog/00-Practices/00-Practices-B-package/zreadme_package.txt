###################################################################
# Structure the Flask_Blog to python package
###################################################################

D:\Education\learn_html\code_snippets\Python\Flask_Blog\05-Package-Structure>tree /F
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

