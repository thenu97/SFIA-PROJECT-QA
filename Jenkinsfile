pipeline {
    agent any

    stages {
        stage('Development Environment') {
            steps {
                    sh 'chmod +x ./script/*' 
                    sh './script/before_installation.sh' 
                    sh './script/installation.sh'
                    sh 'sudo cp /var/lib/jenkins/workspace/pipeline/script/flask.service /etc/systemd/system'
                    sh 'sudo systemctl daemon-reload'
                    sh 'sudo systemctl enable flask.service'
                    sh 'sudo systemctl start flask.service'
                    sh 'sudo systemctl status flask.service'
                    sh 'sudo systemctl restart flask.service'

            }
        }
    }
}
