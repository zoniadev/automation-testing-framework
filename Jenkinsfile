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
                    # Install system dependencies
                    sudo apt-get update
                    sudo apt-get install -y \\
                        libwoff1 \\
                        libevent-2.1-7 \\
                        libopus0 \\
                        libgstreamer-plugins-base1.0-0 \\
                        libgstreamer1.0-0 \\
                        libharfbuzz-icu0 \\
                        libhyphen0 \\
                        libmanette-0.2-0 \\
                        libflite1 \\
                        libgles2 \\

                    # Set up Python
                    python -m venv venv
                    source venv/bin/activate

                    # Install dependencies
                    pip install -r requirements.txt

                    # Install Playwright browsers
                    playwright install chromium
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