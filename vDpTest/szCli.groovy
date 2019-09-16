pipeline {
    agent any
    stages {
        stage('Test file') {
            steps {
                echo 'Test'
                sh 'python3 vDpTest/szCli.py'
            }
        }
    }
}
