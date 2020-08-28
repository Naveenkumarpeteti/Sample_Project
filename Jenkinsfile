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
             echo 'python test.py'
             }
         }
       }
     }
        
        
         
         
