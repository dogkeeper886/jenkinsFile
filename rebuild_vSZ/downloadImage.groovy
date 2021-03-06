pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.1.2.0.277', description: 'Input SZ version')        
    }
    stages {
        stage('Download Image') {                        
            steps {
                echo 'Download start'
                sh 'python3 rebuild_vSZ/getQcow2.py'
            }
        }
        /*stage('Login OpenStack') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('openstack')
            }
            steps {
                echo 'Login start'
                sh 'python3 rebuild_vSZ/identity_auth_tokens.py'
            }
        }
        stage('Image Upload') {
            steps{
                echo 'Upload start'
                sh 'python3 rebuild_vSZ/image_list.py'
            }
        }*/
    }
}
