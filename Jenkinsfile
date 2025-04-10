pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    triggers {
        githubPush() // This enables webhook triggering
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Samruddhikumbhare/My_Portfolio.git', branch: 'master'
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    pip install flake8
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    pip install pytest
                    pytest
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building Python application...'
                // Optional: Add packaging steps
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Optional: run docker-compose, scp files, restart service, etc.
                // sh './deploy.sh'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf $VENV_DIR'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
