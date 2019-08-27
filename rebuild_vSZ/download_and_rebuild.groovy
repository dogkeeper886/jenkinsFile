pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.458', description: 'vsz qcow2 file version')
        //string(name: 'ftpIp', defaultValue: '10.206.5.20', description: 'ftp server ip')
        string(name: 'szIp', defaultValue: '10.206.20.112', description: 'vsz ip address')
    }
    stages {
        stage('Download Image') {                        
            steps {
                echo 'Download start.'
                sh 'python3 rebuild_vSZ/getImg.py $szVer'
            }
        }
        stage('Upload to OpenStack') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('ftp')
            }
            steps {
                echo 'Upload start'
                //sh 'python3 upgrade_vSZ/uploadXimg.py $ftpIp $BITBUCKET_COMMON_CREDS_USR $BITBUCKET_COMMON_CREDS_PSW $szVer'
            }
        }
        stage('Rebuild Instance') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            steps {
                echo 'Rebuild start'
                //sh 'python3 upgrade_vSZ/upgradeScript.py $szIp $BITBUCKET_COMMON_CREDS_USR $BITBUCKET_COMMON_CREDS_PSW $szVer'
            }
        }
    }
}
