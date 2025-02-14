pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.11"  // Update the version to 3.11
        VIRTUAL_ENV_NAME = "venv"
    }

    parameters {
        string(name: 'BRANCH_NAME', description: 'Enter the branch to test (leave blank for default)')
        string(name: 'BEHAVE_TAGS', description: 'Enter Behave tags to run (e.g., @smoke,@ui)')
        booleanParam(name: 'HEADLESS', description: 'Run Playwright in headless mode', defaultValue: true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: params.BRANCH_NAME ?: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/zoniadev/automation-testing-framework.git']]])
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh "python3 -m venv ${VIRTUAL_ENV_NAME}"  // Use "python3" to ensure it uses the correct version
                sh ". ${VIRTUAL_ENV_NAME}/bin/activate && pip install -r requirements.txt"
                sh ". ${VIRTUAL_ENV_NAME}/bin/activate && playwright install"
                sh ". ${VIRTUAL_ENV_NAME}/bin/activate && pip install allure-behave"
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def behaveCommand = ". ${VIRTUAL_ENV_NAME}/bin/activate && behave --format allure_behave.listener --outdir allure-results"

                    if (params.BEHAVE_TAGS) {
                        behaveCommand += " -t '${params.BEHAVE_TAGS}'"
                    }

                    if (params.HEADLESS) {
                        behaveCommand += " -D headless=True"
                    }

                    sh behaveCommand
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