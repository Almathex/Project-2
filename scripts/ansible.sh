#!/bin/sh
pip3 install ansible
ansible-playbook -v -i inventory playbook.yaml -y -y -y
