
1. Add more posts to exercise pagination
    http://127.0.0.1:5000/
            - Log in users
            add more posts for different users
            we can use 'lorem ipsum'

2. Demo pagination in zreadme_pagination.txt

3. Update home() route in routes.py to query with pagination
        def home():
            # 1 tells page default value 
            page = request.args.get('page', 1, type=int)  
            # 5 posts per page     
            posts = Post.query.paginate(page=page, per_page=5) 

4. Update home.html by changing posts to posts.items
      {% for post in posts.items %}

5. test website
    http://127.0.0.1:5000/            # page has default value of 1
    http://127.0.0.1:5000/?page=2     # 5 posts per page  
    http://127.0.0.1:5000/?page=3

    http://127.0.0.1:5000/?page=4     # Not Found since we only have total of 14 posts 








            


      

