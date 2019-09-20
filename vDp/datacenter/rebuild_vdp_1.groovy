pipeline {
    agent any
    stages {
        stage('Rebuild vDP') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('openstack')
                projectName = 'datacenter'
                instanceName = 'vdp-1'
                instanceId = '678d3337-5fad-43b0-9bc9-f47076e859bf'
            }                                
            steps {
                echo 'Rebuild start'
                sh 'python3 vDp/rebuild_instance.py'
            }
        }
        stage('Setup vDp') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
                vdpIp = '192.168.172.10'
                vszIp = '10.206.6.115'
                dpIp = '10.206.20.114'
                dpMask = '255.255.252.0'
                dpGateway = '10.206.23.254'
            }
            steps {
                echo 'Setup start'
                echo 'Wait for vDP start'
                sleep 180
                sh 'python3 vDp/setup_vdp.py'
            }
        }
    }
}
