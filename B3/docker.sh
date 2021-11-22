#!/bin/bash
OUTPUT=$(pwd)
echo "${OUTPUT}"
sudo apt-get install update
sudo apt-get install docker
sudo apt-get install gnome-terminal
cd ${OUTPUT}/Project/Client/
docker build -t client:1.0 .
gnome-terminal -- docker run -it client:1.0 /bin/bash
cd ${OUTPUT}/Project/lambda-image
docker build -t edge:1.0 .
gnome-terminal -- docker run  --cpus="1.5" -p 9001:8080 -v ~/.aws/:/root/.aws/ edge:1.0
gnome-terminal -- docker run -p 9002:8080 -v ~/.aws/:/root/.aws/ edge:1.0
gnome-terminal -- docker stats


