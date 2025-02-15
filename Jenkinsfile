pipeline {
    agent any

    triggers {
        cron('H 22 * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/master']],
                    extensions: [],
                    userRemoteConfigs: [[
                        credentialsId: 'github-pat',
                        url: 'https://github.com/zoniadev/automation-testing-framework.git']]
                )
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    playwright install
                    pip install allure-behave
                '''
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