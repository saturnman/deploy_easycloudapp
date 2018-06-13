#!/bin/bash
apt-get update
apt-get install -y docker.io
docker pull saturnman/easycloudapp
docker run -d -p 10080:80 -v /var/run/docker.sock:/var/run/docker.sock saturnman/easycloudapp
