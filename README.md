# g24-assignment

Population and list of cities application

	This application have the following APIs with UI

	1. Health check of the app (/health)
	2. List of city and its Population (/show_all)
	3. Insert city and population(/insert)
	4. Update population of the city (/update)
	5. Defualt will list all the city and population.

This application is based on the python Django freamwork. We are using the defualt Database of djanog.


Prerequisite:

	Python = 3.8
	Docker = 20.10
	Helm = 3.11
	kubectl = 1.24
	Jenkins and pipline plugin
	AWS EKS k8s cluster and ALB controller deployed on the cluster


Deployments:

Method 1: Jenkins and Jenkins job on k8s

	1. Need to have the jenkins machine with jenkins pipeline plugin installed for grovvy script to execute
	2. Create the pipeline type job and configure the g24-assgiment repo in the URL of jenkins config with creds
    3. Click on Build job with paramertes
    4. Provide the branch name and environment to deploy.
    5. Test the application on the browser or curl using the `test.g24.com`

   This is automated to build the image, push the image to docker hub and deploy into the population namespace using the helm command line


Method 2: Local docker machine

	1. Download the g24-assgingment repo or clone the repo from github
	2. Build the docker image `docker build . -t population`
	3. Run the application `docker run -it -p 80:8000 population:latest`
	4. Test the application using the IP address of the machine on browser or curl call

Method 3: Helm chart on k8s

	Need to Push the docker image to docker hub.
		1. docker login
		2. docker push population:latest'

	1. Create namesapce using the kubectl create ns population
    2. helm upgrade --install -f population/values.yaml population ./population -n population
    3. Test the application on the browser or curl using the `test.g24.com`



Note : Full not ready for production setup
