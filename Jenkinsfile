pipeline {
    agent any

    stages {
        stage('Development Testing') {
            steps {
                    sh 'chmod +x ./script/*' 
                    sh './script/make_script.sh'
                }
            }

        }
    }
