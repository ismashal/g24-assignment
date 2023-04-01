pipeline {
    agent { label 'tools1' }

    parameters {
        string(name: 'BRANCH', defaultValue: '', description: 'Branch name')
        string(name: 'ENVIRONMENT', defaultValue: '', description: 'ENVIRONMENT to deploy stage/prod')
        string(name: 'VERSION', defaultValue: '', description: 'Provide the app version')
    }
    environment {
        ECR_URL = 'docker hub'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: '${BRANCH}', url: 'https://github.com/ismashal/g24-assignment.git'
            }
        }

        stage('Build & Push') {
            steps {
               
                sh 'docker build -t population .'
                sh 'docker tag population:latest $ECR_URL:$VERSION'
                sh 'docker push $ECR_URL:$VERSION'
            }
        }
 
        stage('Deploy Stage') {
            when {
                expression {
                  params.ENVIRONMENT == "stage"
                }
            }   

            steps {

                echo "Deploying on staging $VERSION"

               }
        }

        stage('Deploy Prod') {
            when {

                allOf {
                    params.ENVIRONMENT == "prod"
                    params.BRANCH == "master"
                }
            }

            steps {
                echo "Deploying on prod $VERSION"

            }
        }
    }
}