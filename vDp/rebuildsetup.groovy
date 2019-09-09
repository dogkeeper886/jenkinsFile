pipeline {
    agent any
    stages {
        stage('Rebuild vDP') {
            
            steps {
                echo 'Rebuild start'
            }

        }
        stage('Setup vDp') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('kvm')
            }                        
            steps {
                echo 'Setup start'
                sh 'python3 vDp/setupVdp.py'
            }
        }
    }
}
