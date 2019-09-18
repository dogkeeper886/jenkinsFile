pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.476', description: 'Input SZ version')
        booleanParam(name: 'REBUILD', defaultValue: false, description: 'Rebuild instance')
        booleanParam(name: 'SETUP', defaultValue: false, description: 'Setup instance')

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
        stage('Rebuild vDP') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('openstack')
            }                                
            when { environment name: 'REBUILD', value: 'true' }
            steps {
                echo 'Rebuild start'
                sh 'python3 vDp/rebuildInstance.py'
            }
        }
        stage('Setup vDp') {
            when { environment name: 'SETUP', value: 'true' }

            steps {
                echo 'Setup start'
                echo 'Wait for vDP start'
                sleep 180
                sh 'python3 vDp/setupVdp.py'
            }
        }
    }
}
