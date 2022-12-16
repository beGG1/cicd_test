pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/beGG1/cicd_test.git']]])
            }
        }
        stage('Linter') {
            steps {
                git branch: 'main', url: 'https://github.com/beGG1/cicd_test.git'
                sh 'pip install -r requirements.txt'
                sh 'flake8 .'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}