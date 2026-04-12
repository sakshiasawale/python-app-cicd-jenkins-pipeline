pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                set PYTHONPATH=%WORKSPACE%
                pytest -v --junitxml=results.xml
                '''
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
    }
}