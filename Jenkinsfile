pipeline {

    agent any

    environment {
        // Environment variables will go here later
      GIT_BRANCH = "Develop"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: "$GIT_BRANCH", url: 'https://github.com/nancysingh20/healthwatch-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build') {
            steps {
                 sh 'python -m py_compile app.py'
            }
        }
    }

    post {

        success {
            // What should happen after successful pipeline
        }

        failure {
            // What should happen after failed pipeline
        }

        always {
            // Actions that should always execute
        }
    }
}`
