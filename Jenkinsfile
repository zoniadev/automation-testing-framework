pipeline {
    agent any // Use any available Jenkins agent

    environment {
        PYTHON_VERSION = "3.9" // Or your preferred Python version
        VIRTUAL_ENV_NAME = "venv" // Name of the virtual environment
    }

    parameters {
        string(name: 'BRANCH_NAME', description: 'Enter the branch to test (leave blank for default)')
        string(name: 'BEHAVE_TAGS', description: 'Enter Behave tags to run (e.g., @smoke,@ui)')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: params.BRANCH_NAME ?: '*/main']], extensions: [], userRemoteConfigs: [[url: 'your_git_repository_url']]]) // Replace with your Git URL
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh "python -m venv ${VIRTUAL_ENV_NAME}"
                sh ". ${VIRTUAL_ENV_NAME}/bin/activate" // Activate the virtual environment (Linux/macOS)
                // For Windows: sh ".\\${VIRTUAL_ENV_NAME}\\Scripts\\activate"
                sh "pip install -r requirements.txt"
                sh "playwright install" // Install Playwright browsers
            }
        }

        stage('Run Tests') {
            steps {
                sh ". ${VIRTUAL_ENV_NAME}/bin/activate" // Activate the virtual environment (Linux/macOS)
                // For Windows: sh ".\\${VIRTUAL_ENV_NAME}\\Scripts\\activate"
                if (params.BEHAVE_TAGS) {
                    sh "behave --format allure_behave.listener --outdir allure-results -t \"${params.BEHAVE_TAGS}\""
                } else {
                    sh "behave --format allure_behave.listener --outdir allure-results"
                }
            }
            post {
                always {
                    allure report publisher: true, results: 'allure-results'
                }
            }
        }
    }
}