email: C@demo.com
password: password

- add many posts to demo pagination
- view pagination demo in below
- modify home() route by using paginate, 3 posts per page
- modify home.html 
- update __init__ with rounte07
- test website. (also try   http://localhost:5000?page=2 )
- Add pages' link in home.html
- Add style to the current page in pages' link 
- Edit to reorder posts so the latest post on the top in home() route
- test website


- add user_posts() route to show posts by one author 
- create user_posts.html template
- update href link {{ url_for('user_posts', username=post.author.username) }} for user
  in user_posts.html, post.html. home.html







---------------------------------------
- Demo pagination
---------------------------------------
$ python 
>>> from flaskblog.models import Post
>>> posts = Post.query.paginate()   # get posts in the first page (20 posts per page by default)
>>> posts
<flask_sqlalchemy.Pagination object at 0x00000216576C9B48>
>>> dir(posts)
>>> posts.per_page
20    # default is 20 posts per page
>>> posts.page 
1     # on the first page
>>> for post in posts.items :   
...     print(post)   # would print 20 posts if there are 20 posts or more 
...
Post('First updated post','2021-02-28 04:56:56.054747')
Post('second post','2021-03-01 22:50:33.976068')
Post('third post ','2021-03-01 22:51:01.193460')
:::::::::::::::

>>> posts = Post.query.paginate(per_page=3)
>>> for post in posts.items:
...   print(post)      # print 3 posts on the first page

>>> posts = Post.query.paginate(per_page=3, page=2)
>>> for post in posts.items:
...   print(post)      # print 3 posts on the second page

>>> posts.total        # number of total posts

#########################################################
# page_data.iter_pages() generator can return None
# in the view template, replace None to ...
#########################################################
>>> posts = Post.query.paginate(per_page=1)    # one post per page
>>> for page in posts.iter_pages() :
...    print(page)
...
1
2
3
4
5
None
7
8
>>>

