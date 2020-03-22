pipeline {
    agent any

    stages {
        stage('Testing') {
            steps {
                    sh 'chmod +x ./script/*'
                    sh './script/make_script.sh'
            }
        }
        stage('Development') {
            steps {
                    sh 'chmod +x ./script/*' 
                    sh './script/before_installation.sh' 
                    sh './script/make_service.sh'

            }
        }

    }
}
