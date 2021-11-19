# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /client
#genero il file requirements.txt
COPY requirements.txt requirements.txt
#runno il comando per python
RUN  apt-get update
RUN  apt-get install wget --yes
RUN apt-get install curl --yes
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python","./client.py" ]
