from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

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

# $ python
# >>> import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'ada8419b155676bc78c2296aba9c7c7d'

# http://localhost:5000/
@app.route("/")
@app.route("/home")
def home():
    return render_template('home09_main.html', posts=posts)

# http://localhost:5000/about
@app.route("/about")
def about():
    return render_template('about09_main.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register01.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__' :
    app.run(debug=True)