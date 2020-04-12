#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

apt-get -y update
dpkg-query --show nginx
if [ "$?" != "0" ];
then    
    apt-get -y install nginx
    ufw allow 'Nginx HTTP'
    ufw allow ssh
    ufw allow 'OpenSSH'
fi

sudo mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
sudo echo "we are Holberton students" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "42i \\ \tlocation /hbnb_static/ { \n\t   alias /data/web_static/current/; \n\t   autoindex off; \n\t}" /etc/nginx/sites-available/default

service nginx start
