FROM python:3.5.2-slim

RUN mkdir /app && pip install -U pip flask
WORKDIR /app
