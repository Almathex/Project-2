#!/bin/sh
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 -m venv venv
. venv/bin/activate
cd service1
pip3 install -r requirements.txt
pytest --cov ./application
cd ..
cd service2
pip3 install -r requirements.txt
pytest --cov ./application
cd ..
cd service3
pip3 install -r requirements.txt
pytest --cov ./application
cd ..
cd service4
pip3 install -r requirements.txt
pytest --cov ./application

deactivate

rm -rf venv
