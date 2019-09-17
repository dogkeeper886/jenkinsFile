pipeline {
    agent any
    parameters {
        string(name: 'szVer', defaultValue: '5.2.0.0.476', description: 'Input SZ version')
        booleanParam(name: 'UPGRADE', defaultValue: false, description: 'Upgrade vSZ')
    }
    stages {
        stage('Download file') {
            when { not { expression { fileExists 'vscg-' + szVer + '.ximg' } } }
            steps {
                echo 'File Download '
                sh 'wget http://tdc-repository.arrisi.com:8081/nexus/content/repositories/releases/ruckus/official/mega/sz/5.2.0.0/ML/$szVer/vscg/vscg-$szVer.ximg'
                
            }
        }       
    }
}
