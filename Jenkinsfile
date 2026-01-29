pipeline {
    agent any

    stages {
        stage('Checkout') { steps { checkout scm } }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install pytest pytest-html pytest-cov
                '''
            }
        }

        stage('Build / Compile Check') {
            steps {
                sh '''
                . venv/bin/activate
                python3 -m py_compile app.py
                '''
            }
        }

        stage('Unit Test') {
            steps {
                sh '''
                . venv/bin/activate
                pytest test.py \
                --junitxml=test-reports/results.xml \
                --html=test-reports/report.html \
                --self-contained-html
                '''
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                    publishHTML(target: [
                        reportDir: 'test-reports',
                        reportFiles: 'report.html',
                        reportName: 'Pytest HTML Report'
                    ])
                }
            }
        }
    }

    post {
        success { echo 'Python CI pipeline successful!' }
        failure { echo 'Pipeline failed!' }
    }
}
