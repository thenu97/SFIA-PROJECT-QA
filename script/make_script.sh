#!/bin/bash

source /var/lib/jenkins/bashrc

/var/lib/jenkins/workspace/Pipeline/venv/bin/coverage run --source=. -m pytest /var/lib/jenkins/workspace/Pipeline/tests/testing.py
/var/lib/jenkins/workspace/Pipeline/venv/bin/coverage report -m