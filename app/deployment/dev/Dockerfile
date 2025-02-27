# Use an official Python image as the base
FROM python:3.11-slim AS base

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Copy and install dependencies separately for better caching
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Set environment variables (override at runtime if needed)
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
