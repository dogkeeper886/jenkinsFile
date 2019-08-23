pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.449', description: 'vsz ximg file version')
        string(name: 'ftpIp', defaultValue: '10.206.5.20', description: 'ftp server ip')
        string(name: 'szIp', defaultValue: '10.206.20.109', description: 'vsz ip address')
    }
    stages {
        stage('Download Image') {                        
            steps {
                echo 'Download start.'
                sh 'python3 upgrade_vSZ/getXimg.py $szVer'
            }
        }
        stage('Upload to FTP') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('ftp')
            }
            steps {
                echo 'Upload start'
                sh 'python3 upgrade_vSZ/uploadXimg.py $ftpIp $BITBUCKET_COMMON_CREDS_USR $BITBUCKET_COMMON_CREDS_PSW $szVer'
            }
        }
        stage('Upgrade') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            steps {
                sh 'python3 upgrade_vSZ/upgradeScript.py $szIp $BITBUCKET_COMMON_CREDS_USR $BITBUCKET_COMMON_CREDS_PSW $szVer'
            }
        }
    }
}
