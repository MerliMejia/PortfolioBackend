# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    musl-dev \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app
COPY requirements.txt /app/

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=backend.settings

# Run app.py when the container launches
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
