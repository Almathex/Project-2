# Project-2
QA DevOps Practical Project

Website: http://35.246.21.143:5000/

Trello: https://trello.com/b/qkV41XqE/devops-fundamental-project

Risk Assessment: https://docs.google.com/spreadsheets/d/1KDOYPHiO6hBObNmLxmTj6owbHyyz476xQ-NGfvWHOrs/edit?usp=sharing

# Objective
The objective of the project was: " to create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together." 

The main focus of this project is the deployment of the application.

For this project I should have: 
- Kanban Board: Asana or an equivalent Kanban Board
- Version Control: Git
- CI Server: Jenkins
- Configuration Management: Ansible
- Cloud server: GCP virtual machines
- Containerisation: Docker
- Orchestration Tool: Docker Swarm
- Reverse Proxy: NGINX


# My Approach
I have decided to make an prize genereator application. The app should:

-Use service1 as a front end

-Use service2 and service3 to generate a random number-letter combination, with service2 being the number part and service3 being the letter part.

-Use service4 to generate a reward 

# Summary
Once the app was made I could focus on the backend side, I added a Dockerfile into each of the services to containerize them and made a docker-compose.yaml, I then made ansible related files (Inventory, playbook.yaml and roles/tasks) these help install docker on the (soon-to-be) swarm nodes and then sets up a swarm. I made a Jenkinsfile with scripts so that jenkins can use that to make a pipeline.

I neeed 3 new Virtual Machines: 
- Jenkins
- Manager
- Worker

On the Jenkins machine i started off installing jenkins, once that was complete and set up, I gave jenkins sudo permissions by using sudo visudo and as the jenkins user I installed docker and docker-compose, still as the jenkins user I then generated keys using ssh-keygen -t rsa. I then placed the public key from the jenkins user on the jenkins machine into the Manager and Worker VMs. Once the other two (Manager, Worker) machines where created I used the jenkins machine to ssh into them. I also, still as the jenkins user, did docker login to provide my dockerhub username and password. Then through the jenkins app on port 8080 I set up a webhook for my git repository and enabled it on git, this allows for a rolling update. 

# CI Pipeline
![PIPE](https://github.com/Almathex/Project-2/blob/main/Documentation/pracprojCIPIPE.PNG?raw=True)
# Initial 
![Initial ERD](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/WallFinder-ERD.png?raw=True)

# Trello Board
![Trello Board]

# Risk Assessment
![Risk Assessment]

# Jenkins Build 
![jenkinsBuild](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/Inkedjenkinsbuildtool_LI.jpg?raw=True)

# Testing 
![testing1](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/test.PNG?raw=True)
![Testing](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/pytest.PNG?raw=True)



# Demo
Here is the home page for the app
![Demo1](https://github.com/Almathex/FundamentalProject/blob/main/Documentation/demo1.PNG?raw=True)

# Database



# Room for improvements
