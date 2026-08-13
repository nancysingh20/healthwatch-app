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

        stage('Environment Check') {
            steps {
                sh 'whoami'
                sh 'pwd'
                sh 'uname -a'
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }
        
        stage('Install Dependencies') {
    steps {
        sh '''
            python3 -m venv venv
            venv/bin/pip install -r requirements.txt
        '''
    }
}

        stage('Test') {
    steps {
        sh 'venv/bin/python -m pytest'
    }
}
        stage('Package') {
    steps {
        sh 'tar -czvf healthwatch.tar.gz app.py requirements.txt Dockerfile config/'
    }
}

        stage('Build') {
            steps {
                sh 'venv/bin/python -m py_compile app.py'
            }
        }
    }

    post {

        success {
            // What should happen after successful pipeline
            echo "Successfull"
        }

        failure {
            // What should happen after failed pipeline
            echo "Failed"
        }

        always {
            // Actions that should always execute
           echo "Completed"
        }
    }
}
