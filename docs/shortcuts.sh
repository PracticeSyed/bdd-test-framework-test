#!/bin/bash
# Quick shortcuts for Playwright Framework

# Run complete framework
alias pw-run='python playwright_cli.py "run playwright framework"'

# Extract DOM only
alias pw-extract='python playwright_cli.py "extract dom"'

# Run tests only
alias pw-test='python playwright_cli.py "run tests"'

# Show status
alias pw-status='python playwright_cli.py "show status"'

# Update framework
alias pw-update='python playwright_cli.py "update framework"'

# Setup dependencies
alias pw-setup='python playwright_cli.py "setup framework"'

# Show help
alias pw-help='python playwright_cli.py "help"'

echo "✓ Playwright Framework shortcuts loaded!"
echo ""
echo "Available commands:"
echo "  pw-run      → Run complete framework"
echo "  pw-extract  → Extract DOM"
echo "  pw-test     → Run tests"
echo "  pw-status   → Show status"
echo "  pw-update   → Update framework"
echo "  pw-setup    → Setup dependencies"
echo "  pw-help     → Show help"
