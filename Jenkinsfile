pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '--network host'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
    }
}
