
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1  # Prevent .pyc files
ENV PYTHONUNBUFFERED=1         # Show logs immediately
ENV REPORTS_DIR=/app/reports   # Reports directory
ENV HEADLESS=true              # Default headless mode

WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget unzip curl \
        chromium-driver firefox-esr \
        xvfb libnss3 libgconf-2-4 libxi6 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


RUN mkdir -p /app/reports/allure-results /app/reports/screenshots/passed /app/reports/screenshots/failed


ENV DISPLAY=:99


CMD ["pytest", "--alluredir=/app/reports/allure-results"]
