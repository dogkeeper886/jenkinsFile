pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.476', description: 'Input SZ version')        
    }
    stages {
        stage('Rebuild vDP') {
            input {
                message "Should we rebuild instance?"
                ok "Apply"
                parameters {
                    booleanParam(name: 'REBUILD', defaultValue: true, description: 'rebuild parameter')
            }
            when {
                environment name: 'REBUILD', value: true 
            }
            steps {
                echo 'Rebuild start'
                sh 'ansible -u root kvm -m virt -a "name=vdp state=shutdown"'
                sh 'ansible -u root kvm -m virt -a "name=vdp command=status"'
                sh 'ansible -u root kvm -m file -a "path=/var/lib/libvirt/images/vdp.qcow2 state=absent"'
                sh 'ansible -u root kvm -m copy -a "remote_src=yes src=/var/lib/libvirt/images/vdp-$szVer.qcow2 dest=/var/lib/libvirt/images/vdp.qcow2"'
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
