# Use a base Python image with a specific version (e.g., Python 3.9)
FROM python:3.9-slim

# Set environment variables for Python optimizations
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that your application runs on (if applicable)
EXPOSE 5000

# Define command to run your application
CMD ["python", "app.py"]
