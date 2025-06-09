pipeline {
    agent { label 'local-agent' } // Явно указываем запуск на нужном агенте

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
                    // Построение Docker-образа с тегом из переменной IMAGE_NAME
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Lint') {
            steps {
                // Установка dev-зависимостей и запуск проверки стиля кода
                sh 'pip install -r requirements-dev.txt'
                sh 'flake8 .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    // Логин и пуш образа в DockerHub, используя креденшелы Jenkins
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
