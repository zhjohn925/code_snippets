
$ cd Flask_Blog\00-Practices\H-Posts-3
$ python 

>>> from flaskblog.models import Post
>>> posts = Post.query.all()

>>> for post in posts :
...     print(post)
...
        Post('Blog 2 Xy by user2','2021-03-28 05:31:26.709109')
        Post('Blog 1','2021-04-03 17:47:39.443134')
        ::::::

>>> posts = Post.query.paginate()
>>> posts
        <flask_sqlalchemy.Pagination object at 0x0000028825D2A188>
>>> dir(posts)
        ['__class__', :::, 'has_next', 'has_prev', 'items', 'iter_pages', 
        'next', 'next_num', 'page', 'pages', 'per_page', 'prev', 'prev_num', 
        'query', 'total']

>>> posts.per_page
        20      # 20 post per page

>>> posts.page
1               # the current page

>>> posts.total  # total 14 posts
14

>>> for post in posts.items:
...    print(post)
...
        Post('Blog 2 Xy by user2','2021-03-28 05:31:26.709109')
        Post('Blog 1','2021-04-03 17:47:39.443134')
        Post('Why do we use it?','2021-04-03 17:59:37.163519')
        ::::::

########################################################
# get 5 posts in the first page
########################################################
>>> posts = Post.query.paginate(per_page=5)       # set 5 posts per page
>>> for post in posts.items:
...     print(post)
...                                               
Post('Blog 2 Xy by user2','2021-03-28 05:31:26.709109')
Post('Blog 1','2021-04-03 17:47:39.443134')
Post('Why do we use it?','2021-04-03 17:59:37.163519')
Post('web page editors ','2021-04-03 18:00:12.111351')
Post('What is Lorem Ipsum?','2021-04-03 18:01:24.645851')

########################################################
# get 5 posts in the second page
########################################################
>>> posts = Post.query.paginate(per_page=5, page=2)
>>> for post in posts.items:
...     print(post)
...                                               
Post('the release of Letraset sheets','2021-04-03 18:01:57.451815')
Post('using Lorem Ipsum','2021-04-03 18:02:38.718257')
Post('Where can I get some?','2021-04-03 18:03:25.709345')
Post('a Latin professor','2021-04-03 18:04:03.121023')
Post('consectetur, adipisci velit','2021-04-03 18:05:01.839378')

########################################################
# get posts in the first page, default 20 posts per page
########################################################
>>> posts = Post.query.paginate(page=1)
>>> for post in posts.items:
...     print(post)
...                                        
Post('Blog 2 Xy by user2','2021-03-28 05:31:26.709109')
Post('Blog 1','2021-04-03 17:47:39.443134')
Post('Why do we use it?','2021-04-03 17:59:37.163519')
:::::::

########################################################
# iterate pages
########################################################
        # There are total of 14 posts. 
        # One post per page, so we see 14 pages
        # When there are many pages, we only care about the current page.
        # the other pages can be skipped ('None' can be used for this purpose).
>>> posts = Post.query.paginate(per_page=1)
>>> for page in posts.iter_pages():
...     print(page)
...
        1           
        2
        3
        4
        5
        None        #the other pages are skipped
        13
        14