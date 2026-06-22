#!/bin/bash
echo "Starting MCP Framework..."
echo "Testing Playwright MCP Server..."
npx @playwright/mcp@latest &
PID1=$!
echo "Playwright PID: $PID1"
echo "Framework is running. Press Ctrl+C to stop."
wait
