
1. Create new_post() route in routes.py
            @app.route("/post/new")
            @login_required
            def new_post() :
                return render_template('create_post.html', title='New Post')

2. Create PostForm in forms.py
         - import TextAreaField
         - class PostForm(FlaskForm) :
               title = StringField('Title', validators=[DataRequired()])
               content = TextAreaField('Content', validators=[DataRequired()])
               submit = SubmitField('Post')

3. Add PostForm in new_post() route in routes.py
          - import PostForm
          - @app.route("/post/new", methods=['GET', 'POST'])
            @login_required
            def new_post() :
               form = PostForm()
               if form.validate_on_submit():
                  flash('Your post has been created!', 'success')
                  return redirect(url_for('home'))               
               return render_template('create_post.html', title='New Post', form=form)

4. Create template create_post.html in templates
      - Copy login.html and modify

5. Add new_post navbar in layout.html template in templates
      <a class="nav-item nav-link" href="{{ url_for('new_post') }}">New Post</a>

6. test website
      http://127.0.0.1:5000/
            log in the account and click 'New Post'

      http://127.0.0.1:5000/post/new
            fill in title and content, click 'Post'
            the page is redirect to home page.  
            now we still have dummy post data as defined in posts in routes.py

