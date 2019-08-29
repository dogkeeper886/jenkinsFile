pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.458', description: 'Input SZ version')        
    }
    stages {
        stage('Download Image') {                        
            steps {
                echo 'Download start'
                sh 'python3 rebuild_vSZ/getXimg.py'
            }
        }
    }
}
