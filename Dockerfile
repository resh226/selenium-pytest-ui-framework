# Dockerfile for Selenium Pytest Automation
# Builds Docker image with all dependencies
# Supports headless/non-headless mode

# Base image: lightweight Python 3.11
FROM python:3.11-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1  # Prevent .pyc files
ENV PYTHONUNBUFFERED=1         # Show logs in real-time
ENV REPORTS_DIR=/app/reports   # Path for reports/screenshots
ENV HEADLESS=true              # Default to headless mode

# Set working directory
WORKDIR /app

# Install system dependencies (browser drivers, headless support)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget unzip curl \
        chromium-driver firefox-esr \
        xvfb libnss3 libgconf-2-4 libxi6 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into container
COPY . .

# Create reports directories to avoid permission issues
RUN mkdir -p /app/reports/allure-results /app/reports/screenshots

# Set display port for headless execution
ENV DISPLAY=:99

# Default command: run pytest and generate Allure results
CMD ["pytest", "--alluredir=/app/reports/allure-results", "--headless"]
