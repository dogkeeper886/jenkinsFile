pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.476', description: 'Input SZ version')
        booleanParam(name: 'upgrade', defaultValue: false, description: 'Upgrade vSZ')
        string(name: 'szIp', defaultValue: '10.206.6.115', description: 'Input SZ IP')
    }
    stages {
        stage('Download file') {
            when { not { expression { fileExists 'vscg-' + szVer + '.ximg' } } }
            steps {
                echo 'File Download '
                sh 'wget http://tdc-repository.arrisi.com:8081/nexus/content/repositories/releases/ruckus/official/mega/sz/5.2.0.0/ML/$szVer/vscg/vscg-$szVer.ximg'                
            }
        }
        stage('Copy image to FTP') {
            steps {
                echo 'Copy file vscg-' + szVer + '.ximg to FTP'
                sh 'ansible -u scg ftp -m copy -a "src=$WORKSPACE/vscg-$szVer.ximg dest=/home/scg/"'
            }
        }
        stage('Upgrade SZ') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('vsz')
            }
            when { environment name: 'upgrade', value: 'true' }
            steps {
                echo 'Upgrade start'
                sh 'python3 upgrade_vSZ/upgradeVsz.py'
            }
        }
       
    }
}
