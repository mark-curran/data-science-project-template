# syntax=docker/dockerfile:1

FROM python:3.9-bullseye

WORKDIR /app

COPY .devcontainer/requirements.txt .devcontainer/requirements.txt

RUN pip3 install -r .devcontainer/requirements.txt

COPY . /app
