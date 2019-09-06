pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.476', description: 'Input SZ version')        
    }
    stages {
        stage('Download Image') {                        
            steps {
                echo 'Download start'
                sh 'python3 vDp/getQcow2.py'
            }
        }
        stage('Upload Image to OpenStack') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('openstack')
                //OS_USERNAME = BITBUCKET_COMMON_CREDS_USR
                //OS_PASSWORD = BITBUCKET_COMMON_CREDS_PSW
                OS_PROJECT_NAME = 'lab'
                OS_USER_DOMAIN_NAME = 'Default'
                OS_PROJECT_DOMAIN_NAME = 'Default'
                OS_AUTH_URL = 'http://10.206.6.112:5000/v3'
                OS_IDENTITY_API_VERSION = '3'
            }
            steps {
                echo 'Login start'
                sh 'python3 vDp/glance.py'
            }
        }
        /*stage('Image Upload') {
            steps{
                echo 'Upload start'
                sh 'python3 rebuild_vSZ/image_list.py'
            }
        }*/
    }
}
