pipeline {
    agent any

    parameters {
        string(name: 'BRANCH_NAME', description: 'Enter the branch to test', defaultValue: 'Nikolay')
        string(name: 'BEHAVE_TAGS', description: 'Enter Behave tags', defaultValue: '')
        booleanParam(name: 'HEADLESS', description: 'Run Playwright headless', defaultValue: true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: params.BRANCH_NAME ?: '**']],
                    extensions: [],
                    userRemoteConfigs: [[url: 'https://github.com/zoniadev/automation-testing-framework.git']]
                ])
            }
        }

        stage('Install Dependencies') {  // Corrected and simplified
            steps {
                sh '''
                    /var/jenkins_home/venv/bin/pip install --upgrade pip
                    /var/jenkins_home/venv/bin/pip install -r requirements.txt
                    /var/jenkins_home/venv/bin/playwright install chromium
                    /var/jenkins_home/venv/bin/pip install behave allure-behave
                '''
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def behaveCommand = """
                        behave -f allure_behave.formatter:AllureFormatter -o allure-results
                    """

                    if (params.BEHAVE_TAGS) {
                        behaveCommand += " -t '${params.BEHAVE_TAGS}'"
                    }

                    if (params.HEADLESS) {
                        behaveCommand += " -D headless=True"
                    }

                    sh """
                        Xvfb :99 -screen 0 1280x1024x24 &  # Start xvfb
                        export DISPLAY=:99 # Set display for playwright
                        /var/jenkins_home/venv/bin/behave ${behaveCommand} # Use the venv behave
                    """
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