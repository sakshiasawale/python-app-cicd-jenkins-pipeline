pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest pytest-html pytest-cov
                '''
            }
        }

        stage('Build / Compile Check') {
            steps {
                echo 'Checking Python syntax...'
                bat '''
                    call venv\\Scripts\\activate
                    python -m py_compile app.py
                '''
            }
        }

        stage('Unit Test') {
            steps {
                echo 'Running unit tests with pytest...'
                bat '''
                    call venv\\Scripts\\activate
                    if not exist test-reports mkdir test-reports
                    pytest test.py --junitxml=test-reports\\results.xml --html=test-reports\\report.html --self-contained-html
                '''
            }
            post {
                always {
                    echo 'Archiving test results...'
                    junit 'test-reports/results.xml'
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'test-reports',
                        reportFiles: 'report.html',
                        reportName: 'Pytest HTML Report'
                    ])
                }
            }
        }
    }

    post {
        success {
            echo 'Python CI Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the test results.'
        }
    }
}
