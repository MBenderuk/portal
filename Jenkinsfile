#!groovy

pipeline {
    agent any
    stages {
            stage('Pull latest changes from GitHub') {
               steps {
                     checkout scm
                     }
            }
            stage('Stop Portal on node B') {
             agent { docker { image 'ansible/ubuntu14.04-ansible' } }
              steps {
                    ansiblePlaybook credentialsId: 'fdd41336-1877-48b6-93d2-ec22290f0f26', inventory: '~/ansible/hosts', playbook: 'stop_portal.yml'
                   }  
                    }
            }
}
