#!/bin/bash
#docker build -t cpu_intensive:1.0 .
gnome-terminal -- docker run -p 9001:8080 -v ~/.aws/:/root/.aws/ cpu_intensive:1.0
gnome-terminal -- docker stats


