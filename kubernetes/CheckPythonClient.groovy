pipeline {
   agent any
    environment {
       PYTHON_CLIENT_NAME= sh (returnStdout: true, script: 'kubectl get pods | awk \'/python/{print $1}\'').trim()
    }

   stages {
      stage('PythonClient') {
         steps {
            echo 'Hello World'
            sh label: '', script: 'echo $PYTHON_CLIENT_NAME'
            sh label: '', script: 'kubectl exec $PYTHON_CLIENT_NAME -- ls'

         }
      }
   }
}
