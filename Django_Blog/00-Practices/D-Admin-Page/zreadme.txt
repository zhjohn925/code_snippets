
1. No user table yet. Need to set up database before creating admin user
    - makemigrations just detects the changes, and prepare Django to update the database.
              but does not actually run these changes yet.
       $ django_project> python manage.py makemigrations

    - in order to apply migration, need to run migrate
       $ django_project> python manage.py migrate
          Apply all migrations: admin, auth, contenttypes, sessions
      now, the auth table exists

2. Create django admin user (This would fail if we run this before 1)
        django_project> python manage.py createsuperuser
                Username (leave blank to use 'bear'): user1
                Email address: zhjohn925@hotmail.com
                Password: temp1234
                Password (again): temp1234
                This password is too common.
                Bypass password validation and create user anyway? [y/N]: y
                Superuser created successfully.
        We just create 'user1' is a superuser        

3. Test website
        django_project> python manage.py runserver
                http://127.0.0.1:8000/admin
                login with 'user1' and 'temp1234'
        On the login page, we can create new users. 
        



