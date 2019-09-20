pipeline {
    agent any
    
    stages {
        stage('Rebuild vDP') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('openstack')
            }                                
            steps {
                echo 'Rebuild start'
                sh 'python3 vDp/rebuildInstance.py'
            }
        }
        stage('Setup vDp') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            when { environment name: 'SETUP', value: 'true' }
            steps {
                echo 'Setup start'
                echo 'Wait for vDP start'
                sleep 180
                sh 'python3 vDp/setupVdp.py'
            }
        }
    }
}
