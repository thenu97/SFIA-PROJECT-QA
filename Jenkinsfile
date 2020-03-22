pipeline {
    agent any

    stages {
        stage('Development') {
            steps {
                    sh 'chmod +x ./script/*' 
                    sh './script/before_installation.sh' 
                    sh './script/make_service.sh'
            }
        }
        stage('Testing') {
            steps {
                    sh 'chmod +x ./script/make_script.sh'
                    sh './script/make_script.sh'
            }
        }
    }
}
