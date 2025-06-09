pipeline {
    agent any

    environment {
        IMAGE_NAME = 'valdev111/lesta_fin:latest'
        CREDENTIALS_ID = '981343cb-9b8c-47ec-9a5a-25ca1a8b62e4'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Lint') {
            steps {
                sh 'pip install -r requirements-dev.txt'
                sh 'flake8 .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${CREDENTIALS_ID}") {
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline завершен.'
        }
        failure {
            echo '❌ Pipeline упал.'
        }
    }
}
