from flask import Flask, render_template, url_for

# add variables, use Jinja2 to pass into html
posts = [
    {
        'author': 'Corey Schafer', 'title': 'Blog Post 1',
        'content': 'First post content', 'date_posted': 'April 20, 2018'
    },
        {
        'author': 'Jane Doe', 'title': 'Blog Post 2',
        'content': 'Second post content', 'date_posted': 'April 21, 2018'
    }
]

app = Flask(__name__)

# http://localhost:5000/
@app.route("/")
@app.route("/home")
def home():
    return render_template('home09_main.html', posts=posts)

# http://localhost:5000/about
@app.route("/about")
def about():
    return render_template('about09_main.html', title='About')


if __name__ == '__main__' :
    app.run(debug=True)