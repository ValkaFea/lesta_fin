pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'valdev111/lesta_fin'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/ValkaFea/lesta_fin.git',
                     branch: 'main'
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}:latest").inside {
                        sh '''
                        python -m venv /tmp/venv
                        . /tmp/venv/bin/activate
                        pip install -r requirements-dev.txt
                        flake8 app/
                        '''
                    }
                }
            }
        }

        stage('Push to DockerHub') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-creds') {
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline завершен - очистка...'
            sh 'docker system prune -f'
        }
        success {
            echo '✅ Pipeline успешно выполнен!'
        }
        failure {
            echo '❌ Pipeline завершился с ошибкой'
        }
    }
}