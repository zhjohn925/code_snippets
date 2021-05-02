https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
https://rahul1999.medium.com/deploy-a-flask-app-with-a-sqlite-database-on-heroku-22b5402c5c6
https://roytuts.com/how-to-deploy-python-flask-mysql-based-application-in-heroku-cloud/

- Install flask (try to import flask under python to verify the installation)

$ pip3 install flask
$ pip3 install flask-wtf   # install forms for part 3.


There are two ways to run the script
1. Run flask

$ export FLASK_APP=flaskblog.py   #in Linux
> set FLASK_APP=flaskblog.py      #in Windows

$ export FLASK_DEBUG=1  #Enable debugger. anything changes in the code, no need to restart web server,
> set FLASK_DEBUG=1     #the web browser can pick up after reload.

$ flask run 
Running on http://127.0.0.1:5000/
(Or http://localhost:5000/)

2. Run python script directly 
$ python flaskblog.py


