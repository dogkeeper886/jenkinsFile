pipeline {
    agent any
    parameters {
        string(name: 'fileName', defaultValue: 'MY_FILE_NAME', description: 'Image file name')   
        string(name: 'filePath', defaultValue: 'MY_FILE_PATH', description: 'Where to get file')   
        string(name: 'szIp', defaultValue: 'MY_SZ_IP', description: 'Input SZ IP')
    }
    stages {
        stage('Download and upgrade file') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('ftp')
            }
            steps {
                echo 'Download and upgrade file'
                sh 'python3 backupUpgrade/ftpClient.py $fileName $filePath'                
            }
        }
        stage('Upgrade SZ') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            steps {
                echo 'Upgrade start'
                sh 'python3 backupUpgrade/sshClient.py $szIp $fileName'
            }
        }
       
    }
}
