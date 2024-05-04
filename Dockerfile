# Use an official Ubuntu image as a parent image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY app.py /app

# Set execute permissions for the script (if needed)
RUN chmod +x /app/app.py

# Specify the entry point for the container to be the Python script
ENTRYPOINT ["python", "/app/app.py"]
