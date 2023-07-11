# Use an official Python runtime as a parent image
FROM python:3.10-alpine

RUN apk update && apk add build-base

RUN apk add cmake make g++ curl

# Set the working directory to /app
WORKDIR /app

COPY poetry.lock pyproject.toml /app/

# Install any needed packages specified in requirements.txt
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# Copy the current directory contents into the container at /app
COPY . /app

ENV TELEGRAM_TOKEN=token

# Run app.py when the container launches
CMD ["python3", "main.py"]
