pipeline {
    agent any
<<<<<<< HEAD

    environment {
        PYTHONUNBUFFERED = 1
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                // This is optional if Jenkins is pulling via a webhook
                // git url: 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Set up Python') {
            steps {
                echo 'Setting up Python...'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip setuptools'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '. venv/bin/activate && pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo ' All steps completed successfully.'
        }
        failure {
            echo ' Build or test failed.'
        }
    }
}
=======
>>>>>>> b2b25f3 (Initial commit:  DevSecOps pipeline with Jenkins, Docker, and SonarQube)

    tools {
        python 'Python3' // Make sure you’ve configured this in Jenkins global tools
    }

    stages {
        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\activate && pytest'
            }
        }
    }
}
