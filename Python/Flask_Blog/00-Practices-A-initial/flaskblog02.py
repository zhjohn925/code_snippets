from flask import Flask

# add another route

app = Flask(__name__)

# http://localhost:5000/
@app.route("/")
@app.route("/home")
def home():
    return '<h1>Hello the world!</h1>'

# http://localhost:5000/about
@app.route("/about")
def about():
    return '<h1>About page</h1>'


if __name__ == '__main__' :
    app.run(debug=True)