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
                script {
                    // Use the pre-configured virtual environment
                    sh '''
                        . /venv/bin/activate

                        # Install project-specific requirements
                        pip install -r requirements.txt
                    '''

                    // Optional: Set up any environment variables needed for tests
                    withEnv(['PYTHONPATH=${WORKSPACE}']) {
                        sh 'echo "Python path set to: $PYTHONPATH"'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def behaveCommand = "behave -f allure_behave.formatter:AllureFormatter -o allure-results"

                    if (params.BEHAVE_TAGS) {
                        // Ensure proper quoting of tags
                        behaveCommand += " --tags=${params.BEHAVE_TAGS}"
                    }

                    if (params.HEADLESS) {
                        behaveCommand += " -D headless=True"
                    }

                    sh """
                        # Activate virtual environment
                        . /venv/bin/activate

                        # Print the command for debugging
                        echo "Executing command: ${behaveCommand}"

                        # Run behave
                        ${behaveCommand}
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