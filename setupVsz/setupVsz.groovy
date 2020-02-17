pipeline {
    agent any
    parameters {
        string(name: 'vszIp', defaultValue: 'MY_IP', description: 'Input vSZ ip')
        string(name: 'vszProfile', defaultValue: 'MY_PROFILE', description: '1 for essential 2 for high scale')
        string(name: 'vszIpMode', defaultValue: 'MY_IPMODE', description: '1 for ipv4 2 for ipv6')
    }
    stages {
        stage('Setup start') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            steps {
                echo 'This is setup start'
                sh 'python3 setupVsz/setupVsz.py'
            }
        }
    }
}