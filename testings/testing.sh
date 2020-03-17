#!/bin/bash

source /var/lib/jenkins/workspace/Pipeline/venv/bin/activate

python -m pytest ./tests/testing.py
