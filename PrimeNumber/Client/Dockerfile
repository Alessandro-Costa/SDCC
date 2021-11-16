# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
ADD client.py /
#genero il file requirements.txt
COPY requirements.txt requirements.txt
#runno il comando per python
RUN pip3 install -r requirements.txt
CMD [ "python","./client.py" ]
