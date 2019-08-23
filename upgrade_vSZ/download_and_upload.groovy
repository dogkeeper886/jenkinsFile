pipeline {
    agent any
    stages {
        stage('Download Image') {
            input {
                message "Input vSZ version"
                ok "Apply"
                parameters {
                    string(name: 'szVer', defaultValue: '5.2.0.0.449', description: 'Apply to start pipeline')
                }
            }
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
    }

}
