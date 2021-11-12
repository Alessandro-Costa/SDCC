# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
FROM public.ecr.aws/lambda/python:3.8
#FROM ubuntu
#RUN apt-get update --yes \
#&& apt-get install wget build-essential zlib1g-dev libncurses5-dev vim --yes
COPY app.py ${LAMBDA_TASK_ROOT}
COPY prova ${LAMBDA_TASK_ROOT}
#creo la cartella app
WORKDIR /app
#genero il file requirements.txt
COPY requirements.txt requirements.txt
#runno il comando per python
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY . .
CMD [ "app.handler" ]
