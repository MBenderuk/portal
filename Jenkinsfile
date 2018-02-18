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
              steps {
                    ansiblePlaybook credentialsId: 'fe7f1ab4-14d2-4612-9dae-583a0ab362bb', inventory: '/var/jenkins_home/ansible/hosts', playbook: '/var/jenkins_home/ansible/playbooks/stop_portal.yml'
                   }  
                    }
            }
}
