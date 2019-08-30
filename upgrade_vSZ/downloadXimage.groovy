pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.458', description: 'Input SZ version')        
    }
    stages {
        stage('Download Image') {                        
            steps {
                echo 'Download start'
                sh 'python3 upgrade_vSZ/getXimg.py'
            }
        }
        stage('Upload Image to Ftp') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('ftp')
            }
            steps {
                echo 'Upload start'
                sh 'python3 upgrade_vSZ/ftpUpload.py'
            }
        }
    }
}
