pipeline {
    agent any
    parameters {
        string(name: 'vszIp', defaultValue: 'MY_IP', description: 'Input vSZ ip')
        string(name: 'vszProfile', defaultValue: 'MY_PROFILE', description: '1 for essential 2 for high scale')
        string(name: 'vszIpMode', defaultValue: '1', description: '1 for ipv4 2 for ipv6')
        string(name: 'vszIpType', defaultValue: '2', description: '1 for manual 2 for dhcp')
        string(name: 'vszClusterName', defaultValue: 'MY_CLUSTE', description: 'Cluter Name')
        string(name: 'vszConDes', defaultValue: 'MY_DES', description: 'Controller description')
        string(name: 'vszNatIp', defaultValue: 'MY_NATIP', description: 'Nat ip address')
    }
    stages {
        stage('Setup Network') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            steps {
                echo 'This is setup start'
                sh 'python3 setupVsz/setupVsz.py'
            }
        }
        stage('Setup Cluster') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            steps {
                echo 'This is setup start'
                sh 'python3 setupVsz/setupVsz2.py'
            }
        }
    }
}