#!/bin/sh
sudo su jenkins
pip3 install ansible
~/.local/bin/ansible-playbook -v -i inventory playbook.yaml
