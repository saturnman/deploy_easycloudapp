#!/bin/bash
apt-get update
apt-get install -y docker.io
docker ps  |grep 'saturnman/easycloudapp' |awk '{print $1}'|xargs docker kill
docker ps -a  |grep 'saturnman/easycloudapp' |awk '{print $1}'|xargs docker rm
docker rmi saturnman/easycloudapp
docker pull saturnman/easycloudapp
docker run -d -p 10080:80 -v /var/run/docker.sock:/var/run/docker.sock saturnman/easycloudapp
