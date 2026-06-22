#!/bin/bash
# Quick Start Script for AI BDD Framework

echo "🤖 AI-Powered BDD Test Framework - Quick Start"
echo "================================================"
echo ""

# Check dependencies
echo "📦 Checking dependencies..."
pip list | grep -E "playwright|behave" > /dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    pip install -q playwright behave
    playwright install chromium
fi

echo "✓ Dependencies ready"
echo ""

# Run framework
echo "🚀 Running test framework..."
python run_tests.py

echo ""
echo "================================================"
echo "✨ Framework execution complete!"
echo ""
echo "📊 Check reports in: tests/bdd/reports/"
echo "🔧 Page objects: tests/bdd/pages/page_objects.py"
echo "📝 DOM config: tests/bdd/config/page_objects.json"
