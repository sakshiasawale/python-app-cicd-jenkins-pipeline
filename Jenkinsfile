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
                "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv
                call venv\\Scripts\\activate.bat
                venv\\Scripts\\python.exe -m pip install --upgrade pip
                venv\\Scripts\\pip.exe install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                set PYTHONPATH=%WORKSPACE%
                venv\\Scripts\\pytest.exe -v --junitxml=results.xml
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