pipeline {
   agent any

   stages {
      stage('Kubernetes') {
         steps {
            echo 'Hello World'
            sh label: '', script: 'kubectl get node'
            sh label: '', script: 'kubectl get deployments'
            sh label: '', script: 'kubectl get pods'
            sh label: '', script: 'kubectl get service'
         }
      }
   }
}
