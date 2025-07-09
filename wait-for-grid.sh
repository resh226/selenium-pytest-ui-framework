#!/bin/bash
# -----------------------------------------------------------------------------
# wait-for-grid.sh
# -----------------------------------------------------------------------------
# Waits for Selenium Grid Hub and Nodes to be ready by starting dummy sessions
# -----------------------------------------------------------------------------

GRID_URL="http://selenium-hub:4444"
echo "🔄 Waiting for Selenium Grid by testing dummy sessions (Chrome & Firefox)..."

for i in {1..60}; do
    echo "⏳ Attempt $i: Checking Chrome node..."
    RESPONSE_CHROME=$(curl -s -X POST "$GRID_URL/session" \
        -H "Content-Type: application/json" \
        -d '{"capabilities": {"alwaysMatch": {"browserName": "chrome"}}}')

    if echo "$RESPONSE_CHROME" | grep -q "sessionId"; then
        echo "✅ Chrome node is ready (dummy session started)."
        break
    fi

    echo "⏳ Attempt $i: Checking Firefox node..."
    RESPONSE_FIREFOX=$(curl -s -X POST "$GRID_URL/session" \
        -H "Content-Type: application/json" \
        -d '{"capabilities": {"alwaysMatch": {"browserName": "firefox"}}}')

    if echo "$RESPONSE_FIREFOX" | grep -q "sessionId"; then
        echo "✅ Firefox node is ready (dummy session started)."
        break
    fi

    echo "⏳ Attempt $i: No nodes ready yet..."
    sleep 5
done

if [ $i -eq 60 ]; then
    echo "❌ Timeout: Selenium Grid nodes were not ready after 5 minutes."
    exit 1
fi

echo "🚀 Starting pytest tests..."
exec "$@"
