#!/bin/sh
docker-compose down --rmi all
docker-compose build
