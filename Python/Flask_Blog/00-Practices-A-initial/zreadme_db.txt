$ python
>>> from flaskblog14_db import db
>>> db.create_all()       #creates database structures. site.db is generated.
>>> from flaskblog14_db import User, Post
>>> user_1 = User(username='Corey', email='C@demo.com', password='password')
>>> db.session.add(user_1)
>>> user_2 = User(username='JohnDoe', email='jd@demo.com', password='password')
>>> db.session.add(user_2)
>>> db.session.commit()      #write into database

#### some query examples:
>>> User.query.all()
[User('Corey','C@demo.com','default.jpg'), User('JohnDoe','jd@demo.com','default.jpg')]
>>> User.query.all()[0]
User('Corey','C@demo.com','default.jpg')
>>> User.query.first()
User('Corey','C@demo.com','default.jpg')
>>> User.query.filter_by(username='Corey').all()
[User('Corey','C@demo.com','default.jpg')]
>>> user = User.query.filter_by(username='Corey').first()
>>> user
User('Corey','C@demo.com','default.jpg')
>>> user.id
1
>>> user = User.query.get(1)     # query by id
>>> user
User('Corey','C@demo.com','default.jpg')

##### work with posts
>>> user.posts     # This user has no posts yet
[]

# posts do not pass date_posted, it will take the default current time
>>> post_1 = Post(title='Blog 1', content='First Post Content', user_id=user.id)
>>> post_2 = Post(title='Blog 2', content='Second Post Content', user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.commit()
>>> user.posts
[Post('Blog 1','2021-02-22 23:40:11.581184'), Post('Blog 2','2021-02-22 23:40:11.583159')]
>>> for post in user.posts :
...    print(post.title)
...
Blog 1
Blog 2
>>> post = Post.query.first()
>>> post
Post('Blog 1','2021-02-22 23:40:11.581184')
>>> post.user_id
1
>>> post.author       # 'author' in relationship backref is reference to the user
User('Corey','C@demo.com','default.jpg')

##### refresh the database
>>> db.drop_all()
>>> db.create_all()     # create database table structures
>>> User.query.all()    # database becomes empty
[]
>>> Post.query.all()
[]





