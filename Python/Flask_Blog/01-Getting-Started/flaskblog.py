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


if __name__ == '__main__':
    app.run(debug=True)
