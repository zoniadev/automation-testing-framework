pipeline {
    agent any

    triggers {
        cron('H 22 * * *')
    }

    environment {
        PYTHON_VERSION = "3.11"
        VIRTUAL_ENV_NAME = "venv"
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
                sh "python3 -m venv ${VIRTUAL_ENV_NAME}"
                sh ". ${VIRTUAL_ENV_NAME}/bin/activate && pip install -r requirements.txt"
                sh ". ${VIRTUAL_ENV_NAME}/bin/activate && playwright install"
                sh ". ${VIRTUAL_ENV_NAME}/bin/activate && pip install allure-behave"
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh ". ${VIRTUAL_ENV_NAME}/bin/activate && behave -t @quick -D headless=True -f allure_behave.formatter:AllureFormatter -o allure-results"
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