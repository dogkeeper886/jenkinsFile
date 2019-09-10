pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.476', description: 'Input SZ version')        
    }
    stages {
        stage('Download Image') {                        
            steps {
                echo 'Download start'
                sh 'python3 vDp/getQcow2.py'
            }
        }
        stage('Copy Image to kvm') {
            steps {
                sh 'ansible -u root kvm -m ping'
                sh 'echo "Start file vdp-$szVer.qcow2 to KVM"'
                sh 'printenv'
                sh 'ansible -u root kvm -m copy -a "src=$WORKSPACE/vdp-$szVer.qcow2 dest=/var/lib/libvirt/images/"'
            }
        }
    }
}
