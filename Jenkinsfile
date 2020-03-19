pipeline {
    agent any

    stages {
        stage('Development Environment') {
            steps {
                    sh 'chmod +x ./script/*' 
                    sh './script/before_installation.sh' 
                    sh 'sudo systemctl enable flask.service'
                    sh 'sudo systemctl start flask.service'
                    sh 'sudo systemctl status flask.service'
            }
        }
        stage('Testing'){
            steps {
                    sh 'chmod +x ./script/*' 
                    sh './script/installation2.sh' 
                    sh 'python3 -m pytest ./tests/testing.py'
                    sh 'pip3 show coverage'
                    sh 'python3 -m coverage run -m pytest tests/testing.py'
                    sh 'python3 -m coverage report -m'
                }
            }
        }
    }
