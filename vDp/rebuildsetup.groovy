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
        stage('Copy image to KVM') {
            steps {
                echo 'Copy file vdp-' + szVer + '.qcow2 to KVM'
                sh 'ansible -u root kvm -m copy -a "src=$WORKSPACE/vdp-$szVer.qcow2 dest=/var/lib/libvirt/images/"'
            }
        }
        stage('Rebuild vDP') {                                
            when { environment name: 'REBUILD', value: 'true' }
            steps {
                echo 'Rebuild start'
                sh 'ansible -u root kvm -m virt -a "name=vdp state=shutdown"'
                //sh 'ansible -u root kvm -m virt -a "name=vdp command=status"'
                retry(3) {
                    try {
                        sh 'python3 vDp/statusCheck.py'
                    }
                    catch (exc) {
                        echo 'Something failed, I should sound the klaxons!'
                    }
                    finally {
                        sleep 60
                    }
                }
                sh 'ansible -u root kvm -m file -a "path=/var/lib/libvirt/images/vdp.qcow2 state=absent"'
                sh 'ansible -u root kvm -m copy -a "remote_src=yes src=/var/lib/libvirt/images/vdp-$szVer.qcow2 dest=/var/lib/libvirt/images/vdp.qcow2"'
                sh 'ansible -u root kvm -m virt -a "name=vdp state=running"'
                sh 'ansible -u root kvm -m virt -a "name=vdp command=status"'
            }
        }
        stage('Setup vDp') {
            /*environment {
                BITBUCKET_COMMON_CREDS = credentials('kvm')
            }*/
            when { environment name: 'SETUP', value: 'true' }

            steps {
                echo 'Setup start'
                sh 'python3 vDp/setupVdp.py'
            }
        }
    }
}
