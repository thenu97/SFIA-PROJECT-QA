#!/bin/bash

source /var/lib/jenkins/workspace/Pipeline/venv/bin/activate

python3 -m pytest ./tests/testing.py
