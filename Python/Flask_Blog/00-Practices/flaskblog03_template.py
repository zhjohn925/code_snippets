from flask import Flask, render_template

# add templates

app = Flask(__name__)

# http://localhost:5000/
@app.route("/")
@app.route("/home")
def home():
    return render_template('home01.html')

# http://localhost:5000/about
@app.route("/about")
def about():
    return render_template('about01.html')


if __name__ == '__main__' :
    app.run(debug=True)