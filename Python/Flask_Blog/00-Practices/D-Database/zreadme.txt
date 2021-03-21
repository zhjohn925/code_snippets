
1. Use Flask-SQLAlchemy as database
    $ pip3 install flask-sqlalchemy

2. import SQLAlchemy in flaskblog.py
    from flask_sqlalchemy import SQLAlchemy

3. Specify the URI to tell where is the database located  
       (in flaskblog.py)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site2.db'
    /// indicates the current app directory

4. Create db object (instance) in flaskblog.py
    db = SQLAlchemy(app)

5. database can be present by class  (in flaskblog.py)
   -- Create User model (present as class)
   -- Create Post model (present as class)

6. A relationship is established between two database tables when one table 
    uses a foreign key that references the primary key of another table. 
    This is the basic concept behind the term relational database.

7. play around db operations as in zreadme_db.txt

8. Test website
   $ python flaskblog.py  
        http://127.0.0.1:5000/login

