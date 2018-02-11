pipeline {
    agent any
    stages {
            stage('Stop Portal service on node A') {
               steps {
                    ssh max@A 'sudo service portal stop'
                    sleep 60
                     }
            }
            stage('Start Portal service on node A') {
            steps {
                    ssh max@A 'sudo service portal stop'
                  }

        }
    }
}
