pipeline {
    agent any
    stages {
        environment {
            ftpIp = '10.206.5.20'
            BITBUCKET_COMMON_CREDS = credentials('ftp')
        }
        stage('Download Image') {
            input {
                message "Input vSZ version"
                ok "Apply"
                parameters {
                    string(name: 'szVer', defaultValue: '5.2.0.0.449', description: 'Apply to start pipeline')
                }
            }
            steps {
                sh 'python3 upgrade_vSZ/getXimg.py $szVer'
                sh 'python3 upgrade_vSZ/uploadXimg.py $ftpIp $BITBUCKET_COMMON_CREDS_USR $BITBUCKET_COMMON_CREDS_PSW $szVer'
            }
        }
    }
}
