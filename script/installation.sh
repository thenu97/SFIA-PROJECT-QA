#!/bin/bash

source venv/bin/activate

pip3 install Flask

pip3 install flask_mysqldb

pip3 install flask-bootstrap

pip3 install flask-ckeditor

pip3 install Werkzeug

pip3 install Flask-WTF

python3 -m pip install pytest

pip3 install urllib3

python3 -m pip install coverage

pip3 install selenium

source ~/bashrc

python3 /var/lib/jenkins_home/workspace/pipeline/app.py
