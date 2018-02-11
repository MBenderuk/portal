#!groovy

pipeline {
    agent any
    stages {
            stage('step 1') {
               steps {
                    sh 'pwd'
                    sh 'ls -l'
                     }
            }
            stage('step 2') {
            steps {
                    sh 'cd ~'
                    sh 'pwd'
                  }

        }
    }
}
