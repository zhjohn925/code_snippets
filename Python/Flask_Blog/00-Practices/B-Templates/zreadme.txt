
1. Install flask 

    $ pip3 install flask
    Try to import flask under python to verify the installation

2. Create flaskblog.py

    add root route and home route to the same page:
        @app.route("/")
        @app.route("/home")
        def hello():
            return '<h1>Hello the world!</h1>'

3. two ways to run Flask apps
    --  $ export FLASK_APP=flaskblog.py   
           (\> set FLASK_APP=flaskblog.py in windows )

        $ flask run
            * Debug mode: off
            * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

        $ export FLASK_DEBUG=1      
            # Run app in debug mode. No need to restart the web server,
            # the view is updated when reloading the web browser 
            # if the code changes.
        
        $ flask run
            * Debug mode: on
            * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

    -- $ python flaskblog.py
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

4. Test website:
    http://127.0.0.1:5000/about

    We can see 404 error: page not found

5. add about() route in flaskblog.py

        @app.route("/about")
        def about():
            return '<h1>About page</h1>'

6. Test website:
    http://127.0.0.1:5000/about

    Now we can see about page on the web browser