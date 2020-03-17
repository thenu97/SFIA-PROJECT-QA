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
                    sh 'python3 -m pytest ./tests/testing.py'
                    sh 'chmod +x ./testings/*'
                    sh './testings/testing.sh'
                }
            }
        }
    }
