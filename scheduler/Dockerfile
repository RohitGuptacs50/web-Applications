FROM python:3.7

ENV PYTHONINBUFFERED 1

RUN mkdir /scheduler_app

WORKDIR /scheduler_app

ADD . /scheduler_app

RUN pip install -r requirements.txt