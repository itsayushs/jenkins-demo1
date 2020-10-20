pipeline {
    agent any
    stages {
        stage('install-deps') {
            steps {
                sh 'pip3.8 install -r requirements.txt --user'
            }
        }
        stage('test-run') {
            steps {
                sh 'python3.8 simple_api.py'
            }
        }
	    stage('run-unittest') {
            steps {
		        sh ' python3.8 -m pytest test_test1.py'
            }
        }
    }
}