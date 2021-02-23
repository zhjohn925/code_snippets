from flask import Flask

#Two ways to run this script
# Method 1:
#    $ export FLASK_APP=flaskblog01.py   (in windows: set FLASK_APP=flaskblog01.py)
#    $ export FLASK_DEBUG=1   (No need to restart web server, 
#                  the web browser just reload the page to view the updated html )
#    $ flask run      (kick off web server)
#      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#                   http://localhost:5000 
# Method 2:
#    $ python flaskblog01.py

app = Flask(__name__)

# decorator adds additional functionality into the 
# function (ie. hello() )
@app.route("/")
def hello():
    return '<h1>Hello the world!</h1>'

# __name__ is '__main__' when run this script directly, ie. python flaskblog01.py.
# otherwise, __name__ is the name of module if imported by other scripts. 

# run it by Method 2
if __name__ == '__main__' :
    app.run(debug=True)