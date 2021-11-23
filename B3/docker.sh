#!/bin/bash
OUTPUT=$(pwd)
echo "${OUTPUT}"
sudo apt-get install update
sudo apt-get install docker
sudo apt-get install docker.io
sudo apt-get install gnome-terminal
cd ${OUTPUT}/Project/Client/
docker build -t client:1.0 .
gnome-terminal -- docker run -it client:1.0 /bin/bash
#Avviare l'applicazione solo offline
cd ${OUTPUT}/Project/aws/
docker build -t offline:1.0 .
gnome-terminal -- docker run -p 9001:8080 offline:1.0
gnome-terminal -- docker run -p 9002:8080 offline:1.0
gnome-terminal -- docker stats
#Avviare l'applicazione quando si è in possesso delle credenziali per il servizio Lambda
#cd ${OUTPUT}/Project/lambda-image
#docker build -t edge:1.0 .
#gnome-terminal -- docker run -p 9001:8080 -v ~/.aws/:/root/.aws/ edge:1.0
#gnome-terminal -- docker run -p 9002:8080 -v ~/.aws/:/root/.aws/ edge:1.0
#gnome-terminal -- docker stats


