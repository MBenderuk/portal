#!groovy

pipeline {
    agent any
    stages {
            stage('Pull latest changes from GitHub') {
               steps {
                    checkout scm
                     }
            }
            stage('Stop Portal on node A') {
            steps {
                   sshagent (credentials: ['max']) {
                       sh 'ssh max@10.62.10.199 service portal stop'
                   }  
                  }
            }
     }
}
