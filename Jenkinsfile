pipeline {
    agent any

    parameters {
        string(name: 'BRANCH', defaultValue: '', description: 'Branch name')
        string(name: 'ENVIRONMENT', defaultValue: '', description: 'ENVIRONMENT to deploy stage/prod')
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
                sh 'docker tag population:latest population:latest'
                sh 'docker login'
		        sh 'docker push population:latest'
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
                sh 'helm upgrade --install -f population/values.yaml population ./population -n population'
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
                sh 'helm upgrade --install -f population/values.yaml population ./population -n population'

            }
        }
    }
}
