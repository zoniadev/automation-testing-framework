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
                }  // <-- Here is the missing closing brace for the script block
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def behaveCommand = "behave -f allure_behave.formatter:AllureFormatter -o allure-results --tags=@quick -D headless=True"
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
                    echo 'Cleaning up the workspace...'
                    deleteDir()
                }
            }
        }
    }
}