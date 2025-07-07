#!/bin/bash
# -----------------------------------------------------------------------------
# wait-for-grid.sh
# -----------------------------------------------------------------------------
# Waits for Selenium Grid Hub and Nodes to be ready, then runs pytest tests
# -----------------------------------------------------------------------------

GRID_STATUS_URL="http://selenium-hub:4444/status"

echo "🔄 Waiting for Selenium Grid at $GRID_STATUS_URL..."

# Increase wait attempts: 60 attempts × 5s = 5 minutes total
for i in {1..60}; do
    if curl -s "$GRID_STATUS_URL" | grep '"ready":true' > /dev/null; then
        echo "✅ Selenium Grid is ready!"
        break
    fi
    echo "⏳ Attempt $i: Grid not ready yet..."
    sleep 5
done

if [ $i -eq 60 ]; then
    echo "❌ Timeout: Selenium Grid was not ready after 5 minutes."
    exit 1
fi

echo "🚀 Starting pytest tests..."
pytest --alluredir=/app/reports/allure-results
