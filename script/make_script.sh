#!/bin/bash

source /var/lib/jenkins_home/workspace/pipeline/venv/bin/activate
source /var/lib/jenkins_home/bashrc

/var/lib/jenkins_home/workspace/pipeline/venv/bin/coverage run --omit 'venv/*' -m pytest tests/testing.py
/var/lib/jenkins_home/workspace/pipeline/venv/bin/coverage report -m
