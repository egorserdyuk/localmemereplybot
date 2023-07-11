# Use an official Python runtime as a parent image
FROM python:3.10-alpine

RUN apk update && apk add build-base

RUN apk add cmake make g++

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python -m pip install .

ENV TELEGRAM_TOKEN=token

# Run app.py when the container launches
CMD ["python3", "main.py"]
