pipeline {
    agent any
    stages {
        stage('Rebuild vDP') {           
            steps {
                echo 'Rebuild start'
                sh 'ansible -u root kvm -m virt -a "name=vdp state=shutdown"'
                sh 'ansible -u root kvm -m virt -a "name=vdp command=status"'
                sh 'ansible -u root kvm -m file -a "path=/var/lib/libvirt/images/vdp.qcow2 state=absent"'
                sh 'ansible -u root kvm -m copy -a "remote_src=yes src=$WORKSPACE/vdp-$szVer.qcow2 dest=/var/lib/libvirt/images/vdp.qcow2"'
                sh 'ansible -u root kvm -m virt -a "name=vdp state=running"'
                sh 'ansible -u root kvm -m virt -a "name=vdp command=status"'
            }
        }
        /*stage('Setup vDp') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('kvm')
            }                        
            steps {
                echo 'Setup start'
                sh 'python3 vDp/setupVdp.py'
            }
        }*/
    }
}
