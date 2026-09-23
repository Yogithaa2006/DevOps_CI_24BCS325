pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage started'
                echo 'Python project - no compilation required'
            }
        }

        stage('Test') {
            steps {
                echo 'Running pytest tests'
                bat '"C:\\Users\\Admin\\AppData\\Local\\Python\\bin\\python.exe" -m pytest'
            }
        }

        stage('Result') {
            steps {
                echo 'All build and test stages completed successfully'
            }
        }
    }

    post {
        success {
            echo 'PIPELINE SUCCESS: All stages completed successfully!'
        }

        failure {
            echo 'PIPELINE FAILED: Check the console output.'
        }
    }
}