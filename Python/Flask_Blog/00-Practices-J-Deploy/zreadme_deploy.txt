email: C@demo.com
password: password
email: zhjohn925@hotmail.com
password: 1234

------------------------------------------
- Linode Server (get Ubuntu server)
------------------------------------------
# apt update && apt upgrade                # do update in the first time log in the server   
# hostnamectl set-hostname flask-server    # set host name 
# hostname
flask-server 
# nano /etc/hosts                          # add hostname in the file
127.0.0.1      localhost
45.33.123.214  flask-server
::::::
# adduser star                             # add a user
# adduser star sudo                        # add the user to sudo
# cd /home/star
# mkdir .ssh                               # store public key
------------------------------------------
- Local client window: generate ssh key
------------------------------------------
$ ssh-keygen -b 4096
~/.ssh/id_rsa
~/.ssh/id_rsa.pub
$ scp ~/.ssh/id_rsa.pub  star@<remote_server_ip>:~/.ssh/authorized_keys
------------------------------------------
- Sever: Log out from root and the login as user (star)
------------------------------------------
$ sudo chmod 700 ~/.ssh/
$ sudo chmod 600 ~/.ssh/*
------------------------------------------
- Local client window: ssh log in server no needs password
------------------------------------------
$ ssh star@<server_ip>
$
------------------------------------------
- Sever: modify sshd_config
------------------------------------------
$ sudo nano /etc/ssh/sshd_config
[sudo] password for star:
PermitRootLogin no                # Not allow root to log in to prevent hackers
PasswordAuthentication no         # Use ssh key, no password is needed. Also prevent hackers to use password to log in
$ sudo systemctl restart sshd     # restart ssh server
------------------------------------------
- Sever: install firewall
------------------------------------------
$ sudo apt install ufw               # ufw : uncomplicated firewall
$ sudo ufw default allow outgoing    # allow outgoing traffic
$ sudo ufw default deny incoming     # deny incoming traffic
$ sudo ufw allow ssh                 # allow ssh 
$ sudo ufw allow 5000                # allow port 5000
$ sudo ufw enable                    # enable firewall
$ sudo ufw status                    # view the status
------------------------------------------
- Local client window: deploy
------------------------------------------
$ pip3 freeze > requirements.txt          # list all dependencies 
$ move requirements.txt into Flask_Blog directory want to deploy
$ scp -r Flask_Blog star@<remote-ip>:~/    # copy the whole flask project directory into server
------------------------------------------
- Sever: install python
------------------------------------------
We do not want to use default python. want to run it in virtual environment.
$ sudo apt install python3-pip
$ sudo apt install python3-venv          # allow to create virtual environment
$ python3 -m venv Flask_Blog/venv         # create virtual environment in Flask_Blog
$ cd Flask_Blog
$ pip install -r requirements.txt        # install dependencies for the application (app)
Set environment variables for the app as defined in config.py
    ie. SECRET_KEY="ada8419b155676bc78c2296aba9c7c7d"
    ie. SQLALCHEMY_DATABASE_URI="sqlite:///site.db"
$ sudo touch /etc/config.json
$ sudo nano /etc/config.json
{
    "SECRET_KEY": "ada8419b155676bc78c2296aba9c7c7d", 
    "SQLALCHEMY_DATABASE_URI": "sqlite:///site.db",
    "EMAIL_USER": "Your_GMAIL",
    "EMAIL_PASS": "Your_PASSWORD"
}
------------------------------------------
- Sever: Flask_Blog structure
------------------------------------------
(venv) ~Flask_Blog$ ls 
flaskblog  __pycache__  requirements.txt  run.py  venv
(venv) ~Flask_Blog$ ls flaskblog
config.py  __init__.py  models.py   __pycache__  static   users
errors  main   posts   site.db   templates
------------------------------------------
- Sever: Modify flaskblog/config.py
------------------------------------------
(venv) ~Flask_Blog$ nano flaskblog/config_in_server.py
------------------------------------------
- Sever: Run in development Server
------------------------------------------
(venv) ~Flask_Blog$ export FLASK_APP=run.py
(venv) ~Flask_Blog$ flask run --host=0.0.0.0   
         * Specify the host allows us to access to the server from outside
         * Running on http://0.0.0.0:5000/ 
------------------------------------------
- Local client window: web browser 
------------------------------------------
http://<server-ip>:5000

-------------------------------------------------------------
The ABOVE is to run website in DEVELOPMENT SERVER
-------------------------------------------------------------

------------------------------------------
- Sever: install nginx as web server
------------------------------------------
(venv) ~Flask_Blog$ cd
(venv) ~$ sudo apt install nginx         #install it in virtual environment
(venv) ~$ pip install gunicorn           #install it in virtual environment
(venv) ~$ sudo rm /etc/nginx/sites-enabled/default
(venv) ~$ sudo nano /etc/nginx/sites-enabled/flaskblog

server {
    listen 80;
    server_name <your-server-ip-address>;
    location /static {
        alias /home/star/Flask_Blog/flaskblog/static;
    }
    location / {
        proxy_pass http://localhost:8000;
        include /etc/nginx/proxy_params;
        proxy_redirect off;
    }
}

$ sudo ufw allow http/tcp
$ sudo ufw delete allow 5000
$ sudo ufw enable
$ sudo systemctl restart nginx     


----------------------------------------------------------------------------
Now nginx server starts (listening the port 80), but the server does not 
know how to handle python.
Test website:  http://<server-ip>
would get the errors:
       502 Bad Gateway
So, we need to run gunicorn to handle python.
Number of workers in gunicorn:  2*cores+1
----------------------------------------------------------------------------

(venv) ~$ nproc --all      # find number of cores
1                          # we pick workers = 3  in this case of 1 core
(venv) ~$ cd Flask_Blog
(venv) ~/Flask_Blog$ gunicorn -w 3 run:app    # -w 3     (3 workers)
                                              # run:app  (app in run.py)
      [INFO] Listening at: http://127.0.0.1:8000
      [INFO] Booting worker with pid: 15901
      [INFO] Booting worker with pid: 15902
      [INFO] Booting worker with pid: 15903

------------------------------------------
- Local client window: web browser 
------------------------------------------
Test website:  http://<server-ip>
Now it should work.


------------------------------------------
- Sever: install supervisor
------------------------------------------
(venv) ~/Flask_Blog$ sudo apt install supervisor
(venv) ~/Flask_Blog$ sudo nano /etc/supervisor/conf.d/flaskblog.conf
[progrom:flaskblog]
directory=/home/star/Flask_Blog
command=/home/star/Flask_Blog/venv/bin/gunicorn -w 3 run:app
user=star
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/flaskblog/flaskblog.err.log
stdout_logfile=/var/log/flaskblog/flaskblog.out.log

------------------------------------------
- Sever: generate log
------------------------------------------
(venv) ~/Flask_Blog$ sudo mkdir -p /var/log/flaskblog    # create flaskblog directory if not exists.
(venv) ~/Flask_Blog$ sudo touch /var/log/flaskblog/flaskblog.err.log
(venv) ~/Flask_Blog$ sudo touch /var/log/flaskblog/flaskblog.out.log

(venv) ~/Flask_Blog$ sudo supervisorctl reload

------------------------------------------
- Local client window: web browser 
------------------------------------------
Test website:  http://<server-ip>

Please note: nginx has default max of 2MB file to upload. 
(venv) ~/Flask_Blog$ sudo nano /etc/nginx/nginx.conf
   add:
      client_max_body_size 5M;
(venv) ~/Flask_Blog$ sudo systemctl restart nginx

