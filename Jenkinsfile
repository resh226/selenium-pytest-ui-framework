// ------------------------------------------------------------------------------
// Jenkinsfile
// ------------------------------------------------------------------------------
// Description:
//   - Jenkins CI/CD pipeline for Selenium Pytest automation
//   - Pulls code from GitHub, builds Docker image, spins up Selenium Grid
//   - Runs tests, generates Allure reports, and archives artifacts
//   - Supports screenshots and Allure reports bind-mounted to host
//
// Usage:
//   - Place in repo root and configure Jenkins pipeline to use it
//
// Part of Flow:
//   GitHub → Jenkins → Docker → Selenium Grid → Tests → Allure Reports → Notifications
// ------------------------------------------------------------------------------

pipeline {
    agent any

    environment {
        PROJECT_NAME = 'selenium-pytest-ui'
        ALLURE_RESULTS = 'reports/allure-results'
        ALLURE_REPORT = 'reports/allure-report'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/selenium-pytest-ui-framework.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${PROJECT_NAME}:latest .'
            }
        }

        stage('Run Tests with Docker Compose') {
            steps {
                sh 'docker-compose up --abort-on-container-exit --exit-code-from tests'
            }
        }

        stage('Generate Allure Report') {
            steps {
                // Allure results already bind-mounted in ./reports/allure-results
                sh 'allure generate ${ALLURE_RESULTS} -o ${ALLURE_REPORT} --clean'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: "${ALLURE_REPORT}/**", fingerprint: true
                junit '**/reports/allure-results/*.xml'
            }
        }

        stage('Notify Team') {
            steps {
                mail to: 'reshmasajeevpulickal.com',
                     subject: "Selenium Tests - ${currentBuild.currentResult}",
                     body: "Build ${env.BUILD_NUMBER} finished with status: ${currentBuild.currentResult}"
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean workspace
            sh 'docker-compose down'  // Stop containers
        }
    }
}
