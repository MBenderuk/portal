pipeline {
    agent any
    stages {
            stage('Stop Portal service on node A') {
               steps {
                    sh 'ssh max@10.62.10.199 sudo service portal stop'
                    sleep 60
                     }
            }
            stage('Start Portal service on node A') {
            steps {
                    sh 'ssh max@10.62.10.199 sudo service portal stop'
                  }

        }
    }
}
