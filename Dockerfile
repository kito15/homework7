# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Python script into the Docker container
COPY app.py .

# Run the Python script when the container starts
CMD ["python", "app.py"]
