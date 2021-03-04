
from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


# http://localhost:5000/
@main.route("/")
@main.route("/home")
def home():
    # get page number from url, default is first page (1),
    # the type (int) is used to make sure page is integer.
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home13_paginate.html', posts=posts)


# http://localhost:5000/about
@main.route("/about")
def about():
    return render_template('about11_flash.html', title='About')
