pipeline {
    agent any
    parameters {
        string(name: 'fileName', defaultValue: 'MY_FILE_NAME', description: 'Image file name')   
        string(name: 'filePath', defaultValue: 'MY_FILE_PATH', description: 'Where to get file')   

    }
    stages {
        stage('Check file at image service') {
            environment {
                BITBUCKET_COMMON_CREDS = credentials('openstack')
            }
            steps {
                echo ('Check file at image service')
                sh ('python3 openstack/imageUpload.py $fileName $filePath')
            }
        }
    }
}
