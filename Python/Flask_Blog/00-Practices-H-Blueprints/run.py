from flaskblog import create_app

# flaskblog is package
# import app from flaskblog package

# create the current application (flask.current_app)
# by the default Config
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)