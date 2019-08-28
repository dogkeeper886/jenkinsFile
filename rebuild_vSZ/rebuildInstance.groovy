pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.458', description: 'Input SZ version')        
    }
    stages {
        stage('Login OpenStack') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('openstack')
            }
            steps {
                echo 'Login start'
                sh 'python3 rebuild_vSZ/identity_auth_tokens.py'
            }
        }
    }
}
