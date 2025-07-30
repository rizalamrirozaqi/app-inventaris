pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                sh 'pytest --log-cli-level=INFO > output.log || true'
            }
        }

        stage('Archive Log') {
            steps {
                archiveArtifacts artifacts: 'output.log'
            }
        }

        stage('Export Metrics to Prometheus') {
            steps {
                script {
                    def duration = currentBuild.durationString.replace(' ms', '').toInteger()
                    sh "echo 'jenkins_build_duration_seconds ${duration / 1000}' | curl --data-binary @- http://prometheus:9090/metrics || true"
                }
            }
        }
    }
}