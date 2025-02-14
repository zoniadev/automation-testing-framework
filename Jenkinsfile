pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.9" // Or your preferred Python version
        VIRTUAL_ENV_NAME = "venv" // Name of the virtual environment
    }

    parameters {
        string(name: 'BRANCH_NAME', description: 'Enter the branch to test (leave blank for default)')
        string(name: 'BEHAVE_TAGS', description: 'Enter Behave tags to run (e.g., @smoke,@ui)')
        booleanParam(name: 'HEADLESS', description: 'Run Playwright in headless mode', defaultValue: true) // Added headless option
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: params.BRANCH_NAME ?: '*/main']], extensions: [], userRemoteConfigs: [[url: 'your_git_repository_url']]])
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh "python -m venv ${VIRTUAL_ENV_NAME}"
                sh ". ${VIRTUAL_ENV_NAME}/bin/activate"
                sh "pip install -r requirements.txt"
                sh "playwright install"
                sh "pip install allure-behave"
            }
        }

        stage('Run Tests') {
            steps {
                sh ". ${VIRTUAL_ENV_NAME}/bin/activate"

                def behaveCommand = "behave --format allure_behave.listener --outdir allure-results"

                if (params.BEHAVE_TAGS) {
                    behaveCommand += " -t \"${params.BEHAVE_TAGS}\"" // Correctly quote tags
                }

                if (params.HEADLESS) {
                    behaveCommand += " -D headless=True" // Add headless option
                }

                sh behaveCommand // Execute the constructed command
            }
            post {
                always {
                    allure report publisher: true, results: 'allure-results'
                }
            }
        }
    }
}