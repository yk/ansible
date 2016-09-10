#!/bin/bash

set -x

curl https://raw.githubusercontent.com/yk/ansible/master/roles/tensorflow-from-source/tasks/main.yml > tftasks.yml
curl https://raw.githubusercontent.com/yk/ansible/master/util/install_tensorflow.yml > tf.yml

ansible-playbook tf.yml -c local -i localhost,

rm tf.yml tftasks.yml
