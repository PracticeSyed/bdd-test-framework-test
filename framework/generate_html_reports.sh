#!/bin/bash
# Generate Cucumber HTML Reports

echo "📊 Generating Cucumber HTML Reports..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Installing..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

# Install cucumber-html-reporter globally
if ! command -v cucumber-html-reporter &> /dev/null; then
    echo "📦 Installing cucumber-html-reporter..."
    npm install -g cucumber-html-reporter
fi

# Get latest reports
API_JSON=$(ls -t tests/api/reports/cucumber_*.json 2>/dev/null | head -1)
UI_JSON=$(ls -t tests/bdd/reports/cucumber_*.json 2>/dev/null | head -1)

# Generate API report
if [ -f "$API_JSON" ]; then
    echo "🔌 Generating API HTML report..."
    cucumber-html-reporter \
        --input "$API_JSON" \
        --output "tests/api/reports/cucumber_report.html" \
        --theme bootstrap \
        --name "API Test Report" \
        --brandTitle "Cucumber API Tests"
    echo "✅ API Report: tests/api/reports/cucumber_report.html"
fi

# Generate UI report
if [ -f "$UI_JSON" ]; then
    echo "🖥️  Generating UI HTML report..."
    cucumber-html-reporter \
        --input "$UI_JSON" \
        --output "tests/bdd/reports/cucumber_report.html" \
        --theme bootstrap \
        --name "UI Test Report" \
        --brandTitle "Cucumber UI Tests"
    echo "✅ UI Report: tests/bdd/reports/cucumber_report.html"
fi

echo ""
echo "✅ Done! Open reports in browser:"
echo "   file://$(pwd)/tests/api/reports/cucumber_report.html"
echo "   file://$(pwd)/tests/bdd/reports/cucumber_report.html"
