pipeline {
    agent any

    stages {
        stage('Development Testing') {
            steps {
                    sh 'chmod +x ./script/*' 
                    sh './script/before_installation.sh' 
                    sh 'sudo cp /var/lib/jenkins/workspace/Pipeline/flask.service /etc/systemd/system'
                    sh 'sudo systemctl daemon-reload'
                    sh 'sudo systemctl enable flask.service'
                    sh 'sudo systemctl start flask.service'
                    sh 'sudo systemctl status flask.service'
                    sh 'python3 -m coverage run -m pytest tests/testing.py'
                    sh 'python3 -m coverage report -m'
                }
            }

        }
    }
