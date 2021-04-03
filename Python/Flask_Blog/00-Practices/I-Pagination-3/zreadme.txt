
1. Update home() route to order the posts by date_posted

    def home():
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)

2. test website
    http://127.0.0.1:5000/ 

3. Add user_posts() route in routes.py to view the posts by the specific user

        # copy home() route to modify
        @app.route("/user/<string:username>")
        def user_posts(username):
            page = request.args.get('page', 1, type=int)
            user = User.query.filter_by(username=username).first_or_404()
            posts = Post.query.filter_by(author=user)\
                        .order_by(Post.date_posted.desc())\
                        .paginate(page=page, per_page=2)
            return render_template('user_posts.html', posts=posts, user=user)

4. Create user_posts.html by copying home.html to modify

    <h1 class="m-3">Posts by {{user.username}} ({{posts.total}})</h1>
    
    <a class="mr-2" href="{{ url_for('user_posts', username=post.author.username) }}">{{ post.author.username }}</a>

    {% if posts.page==page_num %}
        <a class="btn btn-info mb-4" href="{{ url_for('user_posts', username=user.username, page=page_num) }}">{{ page_num }}</a>
    {% else %}
        <a class="btn btn-outline-info mb-4" href="{{ url_for('user_posts', username=user.username, page=page_num) }}">{{ page_num }}</a>
    {% endif %}



5. Update home.html and post.html by adding user posts link

    <div class="article-metadata">
        <a class="mr-2" href="{{ url_for('user_posts', username=post.author.username) }}">{{ post.author.username }}</a>


6. test website
    http://127.0.0.1:5000/ 
        Click username link to show the posts by this user only