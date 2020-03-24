#!/bin/bash

source /var/lib/jenkins/workspace/pipeline/venv/bin/activate
source /var/lib/jenkins/bashrc

/var/lib/jenkins/workspace/pipeline/venv/bin/coverage run --omit 'venv/*' -m pytest tests/testing.py
/var/lib/jenkins/workspace/pipeline/venv/bin/coverage report -m
