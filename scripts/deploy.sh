#!/bin/sh
ssh master << EOF
docker pull almathex/service1:latest
docker pull almathex/service2:latest
docker pull almathex/service3:latest
docker pull almathex/service4:latest
docker pull nginx:alpine
git clone https://github.com/almathex/Project-2.git
cd Project-2
sudo docker stack deploy --compose-file docker-compose.yaml randprize
EOF