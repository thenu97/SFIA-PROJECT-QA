#!/bin/bash

sudo cp /var/lib/jenkins/workspace/Pipeline/flask.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable flask.service


sudo systemctl stop flask.service
sudo systemctl start flask.service

source /var/lib/jenkins/bashrc
source /var/lib/jenkins/workspace/Pipeline/venv/bin/activate

/var/lib/jenkins/workspace/Pipeline/venv/bin/coverage run -m pytest /var/lib/jenkins/workspace/Pipeline/tests/testing.py
/var/lib/jenkins/workspace/Pipeline/venv/bin/coverage report -m