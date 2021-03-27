
1. Store post into database in new_post() in routes.py 
        # Construct Post object which defined in models.py
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()

2. Delete the dummy posts data in routes.py

3. Get posts from database in home() route in routes.py
      posts = Post.query.all()

4. test website
      http://127.0.0.1:5000/
            Now we do not have any posts yet
      - log in the account and click 'New Post'
            Now we see the post just being added

5. fix username and date view in home.html template

      <a class="mr-2" href="#">{{ post.author.username }}</a>
      <small class="text-muted">{{ post.date_posted.strftime('%Y-%m-%d') }}</small>

6. add user profile image in home.html template
 


      

