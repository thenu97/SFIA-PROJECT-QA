#!/bin/bash

source venv/bin/activate

sudo pip3 install Flask

sudo pip3 install flask_mysqldb

sudo pip3 install gunicorn

source ~/bashrc

python3 app.py

gunicorn --workers=4 --bind=0.0.0.0:5000 app:app