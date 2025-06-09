pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'valdev111/lesta_fin'
        REMOTE_HOST = 'ubuntu@37.9.53.175'
        REMOTE_DEPLOY_DIR = '/home/ubuntu/lesta_fin'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Cloning repository...'
                git url: 'https://github.com/ValkaFea/lesta_fin.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                script {
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }

        stage('Test / Lint') {
            steps {
                echo '🔍 Running linter...'
                script {
                    docker.image("${DOCKER_IMAGE}:latest").inside {
                        sh '''
                        pip install flake8
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
                echo '📦 Pushing image to DockerHub...'
                script {
                    docker.withRegistry('', 'dockerhub-creds') {
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }

        stage('Deploy to Remote Host') {
            steps {
                echo '🚀 Deploying to remote server via SSH...'
                sshagent (credentials: ['f8aa8db9-0cb7-4195-a4ff-19b1eefe4983']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ${REMOTE_HOST} '
                        set -e

                        echo "Checking if project folder exists..."
                        if [ ! -d "${REMOTE_DEPLOY_DIR}" ]; then
                            echo "Cloning repo..."
                            git clone https://github.com/ValkaFea/lesta_fin.git ${REMOTE_DEPLOY_DIR}
                        else
                            echo "Pulling latest changes..."
                            cd ${REMOTE_DEPLOY_DIR} && git pull
                        fi

                        cd ${REMOTE_DEPLOY_DIR}

                        echo "Pulling Docker image..."
                        docker pull ${DOCKER_IMAGE}:latest

                        echo "Stopping existing containers if any..."
                        /usr/bin/docker-compose down || true

                        echo "Starting containers..."
                        /usr/bin/docker-compose up -d

                        echo "Deployment finished."
                    '
                    """
                }
            }
        }
    }
}
