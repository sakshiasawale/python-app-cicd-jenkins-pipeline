pipeline {
    // Use Docker agent
    agent {
        docker {
            image 'python:3.12-slim'
            args '--network host'  // <-- THIS LINE ensures the container can access GitHub
        }
    }

    stages {

        stage('Checkout') {
            steps {
                // Checkout your GitHub repository
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
    }
}
