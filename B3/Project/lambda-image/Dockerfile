# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
FROM public.ecr.aws/lambda/python:3.8
COPY app.py ${LAMBDA_TASK_ROOT}

RUN mkdir ~/.aws
COPY credentials ~/.aws/credentials
#creo la cartella app
WORKDIR /app
#genero il file requirements.txt
COPY requirements.txt requirements.txt

#runno il comando per python
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY . .
CMD [ "app.handler" ]
