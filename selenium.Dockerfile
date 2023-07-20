FROM ubuntu

USER root
RUN apt-get update
RUN apt-get install wget vim python3 python3-pip -y

RUN ln /usr/bin/python3 /usr/bin/python

COPY requirements.txt .

RUN mrdir "project"
WORKDIR project

RUN python -m pip install -r ./requirements.txt