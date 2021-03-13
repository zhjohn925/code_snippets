
################################################
# The Django web framework includes a default object-relational mapping layer (ORM) 
# that can be used to interact with application data from various relational databases 
# such as SQLite, PostgreSQL and MySQL.
# We can use different databases without changing the codes
################################################

1. Add Post table in blog/models.py

2. Re-run migration to update the database
   - Create migration: 
        below shows make migration in 'blog\migrations\0001_initial.py'
        blog is app, 0001 is migration number
   $ django_project> python manage.py makemigrations
          Migrations for 'blog':
            blog\migrations\0001_initial.py
              - Create model Post

   - Show the SQL command to create Post table
   $ django_project> python manage.py sqlmigrate blog 0001
           :::::::
           CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
           :::::::

   - Run migrate command, commit the Post table to the database.
   $ django_project> python manage.py migrate
           Operations to perform:
           Apply all migrations: admin, auth, blog, contenttypes, sessions
           Running migrations:
           Applying blog.0001_initial... OK

3. Migrations are very useful to create and update database. 
        We can also use Django python shell command to operate the database
   $ django_project> python manage.py shell
           >>> from blog.models import Post
           >>> from django.contrib.auth.models import User
           >>> User.objects.all()
           <QuerySet [<User: user1>]>     # was created in previous section
           >>> User.objects.first()
           <User: user1>
           >>> User.objects.filter(username='user1')
           <QuerySet [<User: user1>]>
           >>> User.objects.filter(username='user1').first()
           <User: user1>
           >>> user = User.objects.filter(username='user1').first()
           >>> user
           <User: user1>
           >>> user.id
           1
           >>> user.pk
           1
           >>> user = User.objects.get(id=1)
           >>> user
           <User: user1>
           >>> post1 = Post(title='Blog 1', content='The first blog', author=user)
           >>> post1 = Post(title='Blog 1', content='The first blog', author=user)
           >>> post1.save()
           >>> Post.objects.all()
           <QuerySet [<Post: Post object (1)>]>
           >>> post1.date_posted
           datetime.datetime(2021, 3, 11, 6, 23, 3, 563460, tzinfo=<UTC>)
           >>> exit()   # if any changes in the codes

   $ django_project> python manage.py shell
           >>> from blog.models import Post
           >>> from django.contrib.auth.models import User
           >>> User.objects.all()
           <QuerySet [<User: user1>]>  
           >>> Post.objects.all()
           <QuerySet [<Post: Blog 1>]>   # print post title as Post.__str__()
           >>> Post.objects.first()
           <Post: Blog 1>      # print post title as Post.__str__()
           >>> user = User.objects.filter(username='user1').first()
           >>> user
           <User: user1>
           >>> user.id
           1
           >>> post2 = Post(title='Blog 2', content='The content in second post', author_id=user.id)
           >>> post2.save()
           >>> Post.objects.all()
           <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
           >>> post = Post.objects.first()
           >>> post.content
           'The first blog'
           >>> post.date_posted
           datetime.datetime(2021, 3, 11, 6, 23, 3, 563460, tzinfo=<UTC>)
           >>> post.author
           <User: user1>       # user object
           >>> post.author.email
           'zhjohn925@hotmail.com'
           >>> user.post_set.all()
           <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>

           # Create a new post by the user via post_set.
           # Django automatically saves the post
           >>> user.post_set.create(title='Blog 3', content="this is blog 3 content")
           <Post: Blog 3>
           >>> Post.objects.all()
           <QuerySet [<Post: Blog 1>, <Post: Blog 2>, <Post: Blog 3>]>
           >>> exit()

4. update blog/views.py by reading posts from database (models)
        from .models import Post
        context = { 'posts': Post.objects.all() }

5. update date view format in blog/templates/blog/home.html
   by using pipe (|) and the format specifier (date:"F d, Y")
        <small class="text-muted">{{ post.date_posted|date:"F d, Y" }}</small>
      
      we can google "django date format"
        https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-date
        - F	Month, textual, long.	'January'
        - d	Day of the month, 2 digits with leading zeros.
        - Y	Year, 4 digits.	'1999'

6. Register Post in blog/admin.py to add Post in admin page

       Now we can manipulate Post database in admin page
       http://127.0.0.1:8000/admin
       user: user1
       pwd:  temp1234





