pipeline{
  agent any
  stages {
      stage('build') {
            steps {
                sh 'python calc.py'
            }
        }
       stage('test'){
        steps{
             sh 'python test.py'
             }
         }
       }
     }
        
        
         
         
