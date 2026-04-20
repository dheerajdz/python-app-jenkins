pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'dheerajdz/my-cicd-app'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                bat 'pytest test_app.py -v'
            }
        }
        
        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
                bat "docker build -t %IMAGE_NAME%:latest ."
            }
        }
        
        stage('Docker Push') {
            steps {
                echo 'Logging in to DockerHub...'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                    bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
                    bat "docker push %IMAGE_NAME%:latest"
                    bat 'docker logout'
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
        }
        success {
            echo 'Build and push successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}