#!/bin/bash

source venv/bin/activate

pip3 install Flask

pip3 install flask_mysqldb

pip3 install flask-bootstrap

pip3 install flask-ckeditor

pip3 install Werkzeug

pip3 install Flask-WTF

source ~/bashrc

python3 /var/lib/jenkins/workspace/Pipeline/venv/bin/app.py
