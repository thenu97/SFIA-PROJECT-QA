#!/bin/bash

source /var/lib/jenkins/bashrc

python3 -m /var/lib/jenkins/workspace/Pipeline/venv/bin/coverage run --source=. -m pytest /var/lib/jenkins/workspace/Pipeline/tests/testing.py
python3 -m /var/lib/jenkins/workspace/Pipeline/venv/bin/coverage report -m