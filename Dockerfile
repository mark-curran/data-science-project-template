# syntax=docker/dockerfile:1
FROM python:3.9-bullseye

WORKDIR /tmp/docker_build
ARG REQUIREMENTS_FILE

# Install requirements.
COPY ${REQUIREMENTS_FILE} /tmp/docker_build/${REQUIREMENTS_FILE}
RUN pip3 install -r /tmp/docker_build/${REQUIREMENTS_FILE}

# Copy the current contents of ./app to the /app directory inside the container.
COPY ./app /app

# Cleanup once build is finished.
RUN rm -rf /tmp/docker_build
