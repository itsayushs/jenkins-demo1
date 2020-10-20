pipeline {
    agent any
    stages {
        stage('install-deps') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test-run') {
            steps {
                sh 'python3 simple_api.py'
            }
        }
	    stage('run-unittest') {
            steps {
		        sh 'pytest test_test1.py'
            }
        }
    }
}