from flask import Flask, render_template

app = Flask(__name__)

# decorator adds additional functionality into the function
# apply route decorator
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

# __name__ is '__main__' when run this script directly, ie. python flaskblog01.py.
# otherwise, __name__ is the name of module if imported by other scripts. 

# debug=True : run app in debug mode
#   No need to restart the web server, the view is updated 
#   when reloading the web browser if the code changes.
if __name__ == '__main__' :
    app.run(debug=True)