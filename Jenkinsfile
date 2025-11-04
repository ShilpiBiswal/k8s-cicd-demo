pipeline {
    agent any

    environment {
        DOCKER_HUB = 'shilpibiswal/student-dashboard'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/ShilpiBiswal/k8s-cicd-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_HUB:$BUILD_NUMBER .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                // Use Username + Password credentials
                withCredentials([usernamePassword(credentialsId: 'dockerhub-token', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $DOCKER_HUB:$BUILD_NUMBER
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}
