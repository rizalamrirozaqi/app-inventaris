pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install --break-system-packages -r requirements.txt'
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
                    def durationMs = currentBuild.duration ?: 0
                    def durationSeconds = durationMs / 1000
                    sh "echo 'jenkins_build_duration_seconds ${durationSeconds}' | curl --data-binary @- http://prometheus:9090/metrics || true"
                }
            }
        }
    }
}
