pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.', description: 'Input SZ version')
        string(name: 'projectName', defaultValue: 'MY_PROJECT', description: 'Input project name')
        string(name: 'instanceId', defaultValue: 'MY_ID', description: 'Input instance id')
        string(name: 'instanceName', defaultValue: 'MY_NAME', description: 'Input instance name')
        string(name: 'vdpIp', defaultValue: 'MY_IP', description: 'Input vDP ip')
        string(name: 'vszIp', defaultValue: 'MY_IP', description: 'Input vSZ ip')
    }
    stages {
        stage('Download file') {
            when { not { expression { fileExists 'vdp-' + szVer + '.qcow2' } } }
            steps {
                echo 'File Download '
                sh 'wget http://tdc-repository.arrisi.com:8081/nexus/content/repositories/releases/ruckus/official/mega/sz/5.2.0.0/ML/$szVer/vdp/vdp-$szVer.qcow2'
            }
        }
        stage('Upload image to openstack') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('openstack')
            }
            steps {
                echo 'Upload file vdp-' + szVer + '.qcow2 to Openstack'
                sh 'python3 vDp/uploadImage.py'
            }
        }
        stage('Rebuild start') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('openstack')
            }
            steps {
                echo 'This is rebuild start'
                sh 'python3 vDp/rebuildInstance.py'
            }
        }
        stage('Setup start') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            steps {
                echo 'This is setup start'
                echo 'Wait for vDP start'
                sleep 180
                sh 'python3 vDp/setupVdp.py'
            }
        }
    }
}