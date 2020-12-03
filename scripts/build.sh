#!/bin/sh
sudo docker-compose down --rmi all
sudo docker-compose build
