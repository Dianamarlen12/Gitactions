FROM ubuntu:20.04

LABEL description = "Actions"
LABEL mainteiner = "Diana Marlen Meneses Alegria"
LABEL version = "v1"

RUN apt-get update

RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip install pytest