# syntax=docker/dockerfile:1

FROM python:3.9-bullseye

# Change this to a different directory, e.g., /tmp/docker_build?
WORKDIR /tmp/docker_build

# Install requirements.
COPY requirements.txt /tmp/docker_build/requirements.txt
RUN pip3 install -r /tmp/docker_build/requirements.txt

# Copy the current contents of ./app to the /app directory inside the container.
COPY ./app /app
