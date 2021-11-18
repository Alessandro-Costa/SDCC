#!/bin/bash
OUTPUT=$(pwd)
echo "${OUTPUT}"
cd ${OUTPUT}/PrimeNumber/Client/
docker build -t client:1.0 .
gnome-terminal -- docker run -it client:1.0 /bin/bash
cd ${OUTPUT}/PrimeNumber/lambda-image
docker build -t edge:1.0 .
gnome-terminal -- docker run -p 9001:8080 -v ~/.aws/:/root/.aws/ edge:1.0
gnome-terminal -- docker run -p 9002:8080 -v ~/.aws/:/root/.aws/ edge:1.0
gnome-terminal -- docker stats


