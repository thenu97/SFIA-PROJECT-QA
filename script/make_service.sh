#!/bin/bash
source /var/lib/jenkins/workspace/pipeline/venv/bin/activate


sudo cp /var/lib/jenkins/workspace/pipeline/flask.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable flask.service


sudo systemctl stop flask.service
sudo systemctl start flask.service
