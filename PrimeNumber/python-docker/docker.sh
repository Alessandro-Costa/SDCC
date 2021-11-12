#!/bin/bash
SCRIPT_PATH="/home/alessandro/PycharmProjects/PrimeNumber/python-docker/curl.sh"
docker build -t cpu_intensive:1.0 .
docker run -p 9001:8080 -v ~/.aws/:/root/.aws/ cpu_intensive:1.0

