#!/bin/bash

set -x

curl https://raw.githubusercontent.com/yk/ansible/master/roles/fb-torch-rocks-cuda/tasks/main.yml > fbtasks.yml
curl https://raw.githubusercontent.com/yk/ansible/master/util/install_torch_and_fb_rocks.yml > fbpb.yml

ansible-playbook fbpb.yml -c local -i localhost,

rm fbpb.yml fbtasks.yml
