# imranmacpy
Flask based personal website

What did I install, in order: 

MacOS/Linux/Unix instructions

brew (ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)") (for mac) for linux: sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
python3 - (brew install python3)
brew tap mongodb/brew
brew install mongodb-community
brew serivces start mongodb-community  [  mongod --config /home/linuxbrew/.linuxbrew/etc/mongod.conf
]
python3 -m venv env2
source env2/bin/activate
pip install flask (pip3)
pip install --upgrade pip
pip install flask-wtf
pip install pycountry
pip install Flask-PyMongo
flask run [--host='0.0.0.0' --port=5001 --debug=true --options=....]


Windows/CMD Instructions

.\env1\Scripts\activate
flask run 

AWS Instructions:

sudo yum update
sudo yum install git -y
git clone https://github.com/immacmillan/imranmacpy.git
cd imranmacpy/
sudo apt-get install build-essential
sudo yum groupinstall 'Development Tools'
yum clean all
yum update glibc
package-cleanup --cleandupes
rpm --rebuilddb
vi mongodb-org-4.2.repo --- make sure it has the right URL
yum install -y mongodb-org
service mongod start
service --status-all
wget https://s3.amazonaws.com/aaronsilber/public/authbind-2.1.1-0.1.x86_64.rpm
rpm -Uvh https://s3.amazonaws.com/aaronsilber/public/authbind-2.1.1-0.1.x86_64.rpm

run("kill `cat /home/ec2-user/imranmacpy/env2/bin/gunicorn.pid`")


in pyenv --- gunicorn:: pip install gunicorn

authbind --deep gunicorn --bind 0.0.0.0:80 wsgi:app
    exec gunicorn --workers 1 --bind unix:imranmacpy.sock wsgi:app >> /var/log/
    exec authbind --deep gunicorn --bind 0.0.0.0:80 wsgi:app >> /var/log/
    gunicorn options: for prod...--access-logfile .log/access.log --error-logfile .log/general.log

additional nginx options:

server {
 server_name <server_name/public ip>;
 listen 80 default_server;
 location / {
 root <full path to the folder containing the index file>;
 index index.html;
 }
location /app {
 rewrite ^/app/(.*) /$1 break;
 proxy_pass http://127.0.0.1:8000;
 proxy_set_header Host $host;
 proxy_set_header X-Real-IP ip_address;
 }
}

