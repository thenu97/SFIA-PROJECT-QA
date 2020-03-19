#!/bin/bash

source /var/lib/jenkins/bashrc
source /var/lib/jenkins/workspace/Pipeline/venv/bin/activate

/var/lib/jenkins/workspace/Pipeline/venv/bin/coverage run -m pytest /var/lib/jenkins/workspace/Pipeline/tests/testing.py
/var/lib/jenkins/workspace/Pipeline/venv/bin/coverage report -m