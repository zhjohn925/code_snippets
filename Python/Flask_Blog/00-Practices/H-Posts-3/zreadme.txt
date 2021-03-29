
1. Create post(post_id) route in routes.py

            @app.route("/post/<int:post_id>")
            def post(post_id) :
            # find the post or give page not found 404 error
            post = Post.query.get_or_404(post_id)
            return render_template('post.html', title=post.title, post=post)

2. Create post.html template.  
      Copy home.html and modify to only a single post

3. Edit home.html post link to post() route with post_id

      <h2><a class="article-title" href="{{ url_for('post', post_id=post.id) }}">{{ post.title }}</a></h2>

4. test website
      http://127.0.0.1:5000/
         - Register new user, and add new post
         - We can see posts with different users on home page
         - click one post to a single post
                  http://127.0.0.1:5000/post/1
         - Try a non-existing post id
                  http://127.0.0.1:5000/post/6
            We can see 404 page "Not Found"

5. Create update_post() route in routes.py
          - import abort
          -  @app.route("/post/<int:post_id>/update")
             @login_required
             def update_post(post_id) :
               This is similar in new_post() route, but 'legend' is added
               return render_template('create_post.html', title='Update Post', form=form)

6. Add legend='New Post' in new_post() route.

7. Update create_post.html template to apply 'legend'.

8. test website
    http://127.0.0.1:5000/
            - Log in a user

            - Click a post is not posted by this user
                  ie. http://127.0.0.1:5000/post/1
            - Try  http://127.0.0.1:5000/post/1/update
                  you will see "Forbidden" by abort(403)

            - Click another post is posted by the current user
                  http://127.0.0.1:5000/post/2/update
                  You will see the update form and form fields are empty.

9. Update update_post() route to show form fields.
            form.title.data = post.title
            form.content.data = post.content

10. test website
    http://127.0.0.1:5000/
            - Log in a user
            - Click a post is posted by the current user
                  http://127.0.0.1:5000/post/2/update
                  You will see the update form and form fields.

11. Update update_post() route to store post into database,
      send flash message, 
      and add methods=['GET', 'POST']
      then populate post for 'GET' request (redirect() sends 'GET' request)

            form = PostForm()
            if form.validate_on_submit():
                  # store post into database
                  post.title = form.title.data
                  post.content = form.content.data
                  db.session.commit()
                  flash('Your post has been update!', 'success')
                  # send 'GET' request
                  return redirect(url_for('post', post_id=post.id))
            elif request.method == 'GET':
                  # populate post data
                  form.title.data = post.title
                  form.content.data = post.content
            return render_template('create_post.html', title='Update Post', 
                                    form=form, legend='Update Post')

10. test website
    http://127.0.0.1:5000/
            - Log in a user
            - Click a post is posted by the current user
                  http://127.0.0.1:5000/post/2/update
                  Modify title and content, and click Post.

11. Update post.html by adding 'update' and 'delete' buttons
            - add bootstrap Modal to 'delete' button
            - https://getbootstrap.com/docs/4.0/components/modal/
                  Look for 'Live demo'
            - Copy Modal template in above web page and do changes. 

                {% if post.author == current_user %}
                    <div>
                        <a href="{{ url_for('update_post', post_id=post.id) }}" class="btn btn-secondary btn-sm mt-1 mb-1">Update</a>
                        <button class="btn btn-danger btn-sm m-1" data-toggle="modal" data-target="#deleteModal">Delete</button>
                    </div>
                {% endif %}

            <!-- Modal -->
            <!-- delete modal-body, "Save changes" button. add "delete" button form -->
            <div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="deleteModalLabel" aria-hidden="true">
                  :::::::
            </div>

12. add delete_post() route in routes.py for testing website.

            @app.route("/post/<int:post_id>/delete")
            @login_required
            def delete_post(post_id) :
            pass

13. test website
    http://127.0.0.1:5000/
            - Log in a user
            - Click a post is posted by the current user
            Now we see 'update' and 'delete' buttons
      - click Update to update the post
      - click Delete, we see Modal, then click 'Close'.

14. Update delete_post() route in routes.py

            # "Delete" button in Modal sends POST request to delete the post
            @app.route("/post/<int:post_id>/delete", methods=['POST'])
            @login_required
            def delete_post(post_id) :
            post = Post.query.get_or_404(post_id)
            if post.author != current_user:
                  abort(403)
            db.session.delete(post)
            db.session.commit()
            flash('Your post has been deleted!', 'success')
            return redirect(url_for('home'))
 
15. test website
    http://127.0.0.1:5000/
            - Log in a user
            - Click a post is posted by the current user
            Now we see 'update' and 'delete' buttons
      - click Update to update the post
      - click Delete, we see Modal, then click 'Delete' to delete the post 


      

