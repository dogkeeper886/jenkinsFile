pipeline {
    agent any
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
        stage() {
            input {
                message "Input parameter"
                parameters {
                    string(name: 'szVer', defaultValue: '5.2.0.0.458', description: 'Input SZ version')        
                    choice(name: 'instanceName', choices: ['vSZinstance1', 'vSZinstance2', 'vSZinstance3', 'vSZinstance4'], description: 'Instance Name')
                }
            }
            steps {
                echo "$szVer"
                echo "$choice"
            }
        }
    }
}
