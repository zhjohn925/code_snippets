
1. Update home() route in routes.py to set 1 post per page
        then we have more pages to show page iterate

        def home():
            # 1 tells page default value 
            page = request.args.get('page', 1, type=int)  
            # 1 posts per page     
            posts = Post.query.paginate(page=page, per_page=1) 

2. Update home.html to view page numbers 

        {% for page_num in posts.iter_pages() %}
            {% if page_num %}
                <a class="btn btn-outline-info mb-4" href="{{ url_for('home', page=page_num) }}">{{ page_num }}</a>
            {% else %}
                ...
            {% endif %}
        {% endfor %}

3. test website
    http://127.0.0.1:5000/      
        change per_page in home() route to view the page numbers

4. Set parameters in posts.iter_pages() in home.html template
    to define/tune page numbers view 

        # left_edge:  number of pages on the far left side
        # right_edge: number of pages on the far right side
        # left_current:  number of pages on the left of the current page (not include the current page)
        # right_current: number of pages on the right of the current page (include the current page)
    
    {% for page_num in posts.iter_pages(left_edge=1, right_edge=1, left_current=1, right_current=2) %}

5. test website
    http://127.0.0.1:5000/      
        click the page numbers link

6. Style the current page number different from the other page numbers
    by updating home.html

        {% if posts.page==page_num %}
            <a class="btn btn-info mb-4" href="{{ url_for('home', page=page_num) }}">{{ page_num }}</a>
        {% else %}
            <a class="btn btn-outline-info mb-4" href="{{ url_for('home', page=page_num) }}">{{ page_num }}</a>
        {% endif %}     

7. test website
    http://127.0.0.1:5000/      
        Now we see the current page number filled with blue

8. Change per_page to 2 for now    
     def home():
        page = request.args.get('page', 1, type=int)
        posts = Post.query.paginate(page=page, per_page=2)
        return render_template('home.html', posts=posts)

9. test website
    http://127.0.0.1:5000/ 
      

