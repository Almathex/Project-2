# Project-2 Please go back to commit: eca1ed2a0b6df1ac153cac23c1b21d5612ec1f11
QA DevOps Practical Project

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
Once the app was made , I added a Dockerfile into each of the services to containerize them and made a docker-compose.yaml, I then made ansible related files (Inventory, playbook.yaml and roles/tasks) these help install docker on the (soon-to-be) swarm nodes and then sets up a swarm. I made a Jenkinsfile with scripts so that jenkins can use that to make a pipeline.

I neeed 3 new Virtual Machines: 
- Jenkins
- Manager
- Worker
On the Jenkins machine i started off installing jenkins, once that was complete and set up, I gave jenkins sudo permissions by using sudo visudo and as the jenkins user I installed docker and docker-compose, still as the jenkins user I then generated keys using ssh-keygen -t rsa. I then placed the public key from the jenkins user on the jenkins machine into the Manager and Worker VMs. Once the other two (Manager, Worker) machines where created I used the jenkins machine to ssh into them. I also, still as the jenkins user, did docker login to provide my dockerhub username and password. Then through the jenkins app on port 8080 I set up a webhook for my git repository and enabled it on git, this allows for a rolling update. 

# CI Pipeline
![CIpipe](https://github.com/Almathex/Project-2/blob/main/Documentation/Capture1234.PNG?raw=True)
# ERD
![ERD](https://github.com/Almathex/Project-2/blob/main/Documentation/erd.PNG?raw=True)
# Trello Board
![TRELLO](https://github.com/Almathex/Project-2/blob/main/Documentation/trello.PNG?raw=True)
# Risk Assessment
![RISK](https://github.com/Almathex/Project-2/blob/main/Documentation/Capture14141.PNG?raw=True)
# Service Infrastructure
![Infa](https://github.com/Almathex/Project-2/blob/main/Documentation/infa.PNG?raw=True)
# CI Pipeline
![CIpipe](https://github.com/Almathex/Project-2/blob/main/Documentation/Capture1234.PNG?raw=True)
# GCP
I first spun up a virtual machine on GCP with the purpose of creating the app, placing my local machines public key in, I then SSH through VSC to my VM and clone this GIT repository and create services. Once all the services are complete and the app is working successfully push to Github. I then create a new VM to be my jenkins machine.
# Jenkins Build 
On my jenkins machine I have to first install and unlock Jenkins, once unlocked I use sudo visudo in my VM to add jenkins to be a sudo user. As the jenkins user I then install docker and docker-compose adding the jenkins user to the docker user group, allowing jenkins to use docker without sudo commands, and then restart the terminal. Still as the jenkins user I create keys by typing ssh-keygen -r rsa and then using cat ./.ssh/id_rsa.pub to get jenkins public key. I then go into gcp and spun up two VMs, a manager and a worker maching, making sure I place the public key for jenkins into both. I must SSH into both worker and manager machines through my jenkins machine to generate a key signature. 

In order to make a Jenkins pipeline I need to have a Jenkinsfile for jenkins to read, the pipeline has a number of benefits the main for me is the easily digestible progress tracker, where you can see what stage your build fails at. The Jenkinsfile defines stages and we give it steps for each stage, I choose to execute scripts in my steps as it is easy to impliment. 

Here is a picture of my final jenkins Pipeline:
![STAGE](https://github.com/Almathex/Project-2/blob/main/Documentation/buildlog.PNG?raw=True)

# Testing 
The first stage is testing where I pytest each service using pytest --cov ./application after making a venv and installing pytest.
- service 1 tests are missing as i wrote the tests before adding in a database, and forgot to go back and add them into the script.

service 2,3,4:
![TEST](https://github.com/Almathex/Project-2/blob/main/Documentation/service4test.PNG?raw=True)
# Ansible
The second stage is ansible, which is used to automate the connectivity of a manager and its workers. In order to use ansible I must first create an inventory file in my main directory, this is used to define which VMs is a manager and which are workers, StrictHostKeyChecking=no is also used in the inventory so that jenkins can run asible without getting errors.
I then need to make a playbook.yaml file and define which hosts (defined in the inventory) will have what roles, i then of course need to make roles directory, and create the directories with the same name as the roles defined in the playbook.yaml. In each of the roles I add a new directory called tasks and in each of the respective task directories I make a main.yaml, making sure the .yaml is the same as the playbooks. In the main.yaml I specify the tasks for any node who is assigned to do, for example, my docker role gets both nodes to install docker and perform the nessesary actions, the master role tells my manager node to set up a docker swarm and export the token, and the worker role tells my worker to join the swarm with the token.
![SWARM](https://github.com/Almathex/Project-2/blob/main/Documentation/ansible.PNG?raw=True)
# Docker
I make Dockerfiles in each service in order to build images of them, exposing servies (1,2,3,4) to port 500(0/1/2/3) respectivly. I then make a docker-compose.yaml which makes use of configuration files to build all of the containers at once and builds and deploys them as a service. In my script for the jenkins Pipeline I login to docker (having previously done so), stop and remove any previously running images, build my new images and push them to DockerHub.
![LOGS](https://github.com/Almathex/Project-2/blob/main/Documentation/Screenshot%20.png?raw=True)
Here are my build logs.
# Docker Swarm
I ssh into my swarm manager using StrictHostKeyChecking=no and pull the latest images for my services and clone and move into a directory, I then docker stack deploy accross the swarm using the docker-compose.yaml and giving my stack the name randprize.
# NGINX
I then spin up a NGINX VM on GCP and create a nginx.conf, I then install docker and docker run an NGINX container. 
![NGINX](https://github.com/Almathex/Project-2/blob/main/Documentation/infastr.PNG?raw=True)
Nginx acts as a load balancer and evenly distributes traffic between the manager and worker node.
# Demo
Here is the home page for the app, very simple
![first](https://github.com/Almathex/Project-2/blob/main/Documentation/service1.PNG?raw=True)
Here is the prize page
![last](https://github.com/Almathex/Project-2/blob/main/Documentation/service4.PNG?raw=True)
Yay I won!
# Webhook 
During the demo I was asked to preform a rolling update, I was able to do this by setting up a webhook, first on jenkins then on github using the jenkins ip.
![jenkwebhook](https://github.com/Almathex/Project-2/blob/main/Documentation/jenk.PNG?raw=True)
![gitwebhook](https://github.com/Almathex/Project-2/blob/main/Documentation/webhook.PNG?raw=True)
I am no set up so that any time I push to the repository, jenkins automatically builds and deploys the new version.
![branch](https://github.com/Almathex/Project-2/blob/main/Documentation/branch.PNG?raw=True)
During the demo I merged my develop branch into my main to get the following change, without downtime.
![webhook](https://github.com/Almathex/Project-2/blob/main/Documentation/secondit.PNG?raw=True)
# Database
Here is a working database that persists
![DB](https://github.com/Almathex/Project-2/blob/main/Documentation/db.PNG?raw=True)
# Errors
I had multiple errors throughout this project, it first started with getting the database container set up, an error i have made after setting the database up is leaving sensative infomation in my code. I was also having trouble running NGINX from my jenkins VM so I made another VM only for NGINX which fixed the issue.
