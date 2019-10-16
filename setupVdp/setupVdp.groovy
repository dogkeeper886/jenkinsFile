pipeline {
    agent any
    parameters {
        string(name: 'vdpIp', defaultValue: 'MY_IP', description: 'Input vDP ip')
        string(name: 'vszIp', defaultValue: 'MY_IP', description: 'Input vSZ ip')
    }
    stages {
        stage('Setup start') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            steps {
                echo 'This is setup start'
                sh 'python3 setupVdp/setupVdp.py'
            }
        }
    }
}