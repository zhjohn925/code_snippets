from flask import Flask

#__name__ is name of this module
app = Flask(__name__)

# decorator adds the stuff into the existing functions
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# __name__ is __main__ only when run it standalone, then the condition is True, 
# the functions will be called.
# otherwise, __name__ is the module name when imported by another python, then 
# the condition is False, the functions will not be called.
if __name__ == '__main__':
    app.run(debug=True)
