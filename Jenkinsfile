pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        DEPLOY_CREDENTIALS = credentials('deploy')
    }
    stages {
        stage('CloningGit') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'deploy', url: 'git@github.com:stefobaev/firstDemo.git']]])
            }
        }
        
        stage('DOCKER Build ,Login and push') {
            steps {
                sh 'docker build -t stefobaev/firstdemo:latest /var/lib/jenkins/workspace/last'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push stefobaev/firstdemo:latest'
                sh 'docker rmi stefobaev/firstdemo:latest'
            }
        }
        
        stage('ssh ,pull and deploy') {
            steps {
                script {
                    sh """
                    #!/bin/bash
                    ssh -T -o StrictHostKeyChecking=no -i frankubuntu.pem ubuntu@3.74.162.44 << EOF
                    docker container stop demo
                    docker container rm demo
                    docker rmi -f stefobaev/firstdemo:latest
                    docker pull stefobaev/firstdemo:latest
                    docker run -t -d -p 9999:5000 --name demo stefobaev/firstdemo:latest
                    exit 0
                    << EOF
                    """
                }
            }
        }
    }
}
