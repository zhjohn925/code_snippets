
1. create templates directory

2. create templates/home.html for home() route
   create templates/about.html for about() route

3. render home template in flaskblog.py
    # Flask knows to render html(views) in templates directory
    # change hello() to home() for meaningful function name
    def home():
        return render_template('home.html')

4. render about template in flaskblog.py
    def about():
        return render_template('about.html')

5. Test website
   $ python flaskblog.py
        http://127.0.0.1:5000
        http://127.0.0.1:5000/home
        http://127.0.0.1:5000/about