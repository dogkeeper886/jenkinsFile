pipeline {
    agent any
    parameters {
        string(name: 'serverId', defaultValue: 'Instance ID', description: 'Instance ID')
        string(name: 'imageId', defaultValue: 'Image ID', description: 'Image ID')
    }
    stages {
        stage('Run rebuild') {            
            steps {
                echo 'Run script'
                sh 'python3 openstack/rebuildInstance.py $serverId $imageId'                
            }
        }
    }
}