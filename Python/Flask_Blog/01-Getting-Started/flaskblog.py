from flask import Flask

# __name__ is __main__ if we run this script directly. 
# if it is imported by somewhere else, __name__ is 
# module name
app = Flask(__name__)

# decorator adds the additional functionality into the existing functions.
# route to http://localhost:5000/      ("/" is root page of the web site). 
# route to http://localhost:5000/home 
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

# route to http://localhost:5000/about
# if below is not defined, "404 error" occurs due to the page not found.
@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# __name__ is __main__ only when run it directly, then the condition is True, 
# the functions in if block will be called.
# otherwise, __name__ is the module name when imported by other python scripts, then 
# the condition is False, the functions in if block will not be called.
if __name__ == '__main__':
    # run in debug mode. That means, anything changes, no need to restart web server, 
    # the web browser can pick up after reload. 
    app.run(debug=True)
