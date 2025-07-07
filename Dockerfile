# ------------------------------------------------------------------------------
# Dockerfile for Selenium Pytest Automation
# ------------------------------------------------------------------------------
# Builds a Docker image for running UI tests with Selenium and Pytest
# Supports headless mode and Selenium Grid integration
# ------------------------------------------------------------------------------

# Base Python image
FROM python:3.11-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1  # Prevent .pyc files
ENV PYTHONUNBUFFERED=1         # Show logs immediately
ENV REPORTS_DIR=/app/reports   # Reports directory
ENV HEADLESS=true              # Default headless mode

# Set work directory
WORKDIR /app

# Install system dependencies for headless browsers
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget unzip curl \
        chromium-driver firefox-esr \
        xvfb libnss3 libgconf-2-4 libxi6 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Create folders for Allure and screenshots
RUN mkdir -p /app/reports/allure-results /app/reports/screenshots/passed /app/reports/screenshots/failed

# Set display for headless execution
ENV DISPLAY=:99

# Default command: run pytest and generate Allure results
CMD ["pytest", "--alluredir=/app/reports/allure-results"]
