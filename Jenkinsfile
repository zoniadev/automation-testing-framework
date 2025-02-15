pipeline {
    agent any

    triggers {
        cron('H 22 * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: 'main']],
                    extensions: [],
                    userRemoteConfigs: [[url: 'https://github.com/zoniadev/automation-testing-framework.git', credentialsId: 'github-pat']]
                ])
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh "python3 -m venv venv"
                sh "./venv/bin/activate && pip install -r requirements.txt"
                sh "./venv/bin/activate && playwright install"
                sh "./venv/bin/activate && pip install allure-behave"
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'venv/bin/activate && behave -t @unbroken -D headless=True -f allure_behave.formatter:AllureFormatter -o allure-results'
                }
            }
            post {
                always {
                    allure results: [[path: 'allure-results']]
                }
            }
        }
    }
}