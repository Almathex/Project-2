#!/bin/sh
sudo docker login
sudo docker-compose down --rmi all
sudo docker-compose build
sudo docker-compose push