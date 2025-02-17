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

        stage('Setup Environment and Dependencies') {
            steps {
                sh '''
                    # Check if venv exists, if not create it
                    if [ ! -d "/var/jenkins_home/venv" ]; then
                        python3 -m venv /var/jenkins_home/venv
                    fi

                    # Activate virtual environment
                    . /var/jenkins_home/venv/bin/activate

                    # Install dependencies
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    playwright install chromium
                    pip install behave allure-behave
                '''
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def behaveCommand = """
                        -f allure_behave.formatter:AllureFormatter -o allure-results
                    """

                    if (params.BEHAVE_TAGS) {
                        behaveCommand += " -t '${params.BEHAVE_TAGS}'"
                    }

                    if (params.HEADLESS) {
                        behaveCommand += " -D headless=True"
                    }

                    sh """
                        # Activate virtual environment
                        . /var/jenkins_home/venv/bin/activate

                        # Start Xvfb and wait for it to be ready
                        Xvfb :99 -screen 0 1280x1024x24 &
                        sleep 2  # Give Xvfb time to start

                        # Set display before running tests
                        export DISPLAY=:99

                        # Run behave
                        behave ${behaveCommand}
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