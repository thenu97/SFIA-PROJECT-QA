#!/bin/bash

source /var/lib/jenkins/bashrc

coverage run --source=. -m pytest tests/testing.py
coverage report -m