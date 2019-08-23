pipeline {
    agent any
    environment {
        instanceIP = '10.206.20.109'
        szVer = '5.2.0.0.451'        
    }
    stages {
        stage('Download Image') {
            steps {
                sh 'python3 getImg.py $szVer'
            }
        }
        stage('Uplod to FTP') {
            environment {
                ftpIp = '10.206.5.20'
                BITBUCKET_COMMON_CREDS = credentials('ftp')
            }
            steps {
                sh 'python3 ftpUpload.py $ftpIp $BITBUCKET_COMMON_CREDS_USR $BITBUCKET_COMMON_CREDS_PSW $szVer'
            }
        }
        stage('Upgrade') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            steps {
                sh 'python3 ia.py $instanceIP $BITBUCKET_COMMON_CREDS_USR $BITBUCKET_COMMON_CREDS_PSW $szVer'
            }
        }
    }
}