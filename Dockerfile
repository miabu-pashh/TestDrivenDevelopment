# Use the official Python image from Docker Hub as the base image
# FROM python:3.8-slim

FROM python:3.8-slim-buster
# Set working directory
WORKDIR /usr/src/app
# Copy
COPY test.py .
COPY sparse_recommender.py .

RUN pip install pytest
# CMD []
# run
CMD [ "python", "./test.py" ]