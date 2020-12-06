#!/bin/sh
ssh jenkins@manager -o StrictHostKeyChecking=no << EOF
sudo docker pull almathex/service1:latest
sudo docker pull almathex/service2:latest
sudo docker pull almathex/service3:latest
sudo docker pull almathex/service4:latest
sudo docker pull nginx:alpine
git clone https://github.com/almathex/Project-2.git
cd Project-2
sudo docker stack deploy --compose-file docker-compose.yaml randprize
EOF