pipeline {
    agent any
    parameters {
        string(name: 'TEST_PARAM', description: 'Test parameter')
    }
    stages {
        stage('Test') {
            steps {
                echo "Test parameter: ${params.TEST_PARAM}"
            }
        }
    }
}