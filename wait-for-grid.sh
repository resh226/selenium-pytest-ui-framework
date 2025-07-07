#!/bin/bash
# -----------------------------------------------------------------------------
# wait-for-grid.sh
# -----------------------------------------------------------------------------
# Waits for Selenium Grid to become ready, then runs pytest tests
# -----------------------------------------------------------------------------

echo "🔄 Waiting for Selenium Grid at $GRID_URL..."

for i in {1..30}; do
    if curl -s "$GRID_URL/status" | grep '"ready":true' > /dev/null; then
        echo "✅ Selenium Grid is ready!"
        break
    fi
    echo "⏳ Attempt $i: Grid not ready yet..."
    sleep 5
done

if [ $i -eq 30 ]; then
    echo "❌ Timeout: Selenium Grid was not ready after 150 seconds."
    exit 1
fi

echo "🚀 Starting pytest tests..."
pytest --alluredir=/app/reports/allure-results
