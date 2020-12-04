#!/bin/sh
mkdir -p ~/.local/bin
echo 'PATH=$PATH:home/jenkins/.local/bin' >> ~/.bashrc
source ~/.bashrc
pip3 install --user ansible
/home/jenkins/.local/bin/ansible-playbook -i inventory playbook.yaml