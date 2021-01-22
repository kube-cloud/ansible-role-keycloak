#!/bin/bash

# Log
echo "=================> DATA Directory     : $DOCKER_DATA_DIR" >> $DOCKER_DATA_DIR/env_content.txt
echo "=================> SCRIPTS Directory  : $DOCKER_SCRIPTS_ASSETS_DIR" >> $DOCKER_DATA_DIR/env_content.txt
echo "=================> SECURITY Directory : $DOCKER_SECURITY_ASSETS_DIR" >> $DOCKER_DATA_DIR/env_content.txt

# Install glusterfs docker plugin
docker plugin install --alias glusterfs trajano/glusterfs-volume-plugin --grant-all-permissions --disable

# Set the glusterfs servers
docker plugin set glusterfs SERVERS=127.0.0.1

# Enable glusterfs plugin
docker plugin enable glusterfs