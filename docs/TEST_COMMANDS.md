# 🚀 Test Execution Commands

## Run All Tests (API + UI)
```bash
python run_tests.py
```

## Run Only API Tests
```bash
behave tests/api/features
```

## Run Only UI Tests (Playwright)
```bash
behave tests/bdd/features
```

## Run Specific Feature File
```bash
# API specific feature
behave tests/api/features/api_tests.feature

# UI specific feature
behave tests/bdd/features/practice_site.feature
behave tests/bdd/features/context_aware.feature
```

## Run Specific Scenario
```bash
# By line number
behave tests/api/features/api_tests.feature:3

# By name
behave tests/api/features/api_tests.feature -n "Get all products"
```

## Run with Detailed Output
```bash
# Verbose mode
behave tests/bdd/features -v

# Show skipped tests
behave tests/bdd/features --show-skipped
```

## Generate Reports
```bash
# JSON report
behave tests/api/features -f json -o report.json

# HTML report (via run_tests.py)
python run_tests.py
```

## Quick Commands

### API Only
```bash
cd /home/sagemaker-user/shared
behave tests/api/features
```

### UI Only
```bash
cd /home/sagemaker-user/shared
behave tests/bdd/features
```

### Both with Reports
```bash
cd /home/sagemaker-user/shared
python run_tests.py
```

## View Latest Report
```bash
# Find latest report
ls -lt tests/reports/combined_report_*.html | head -1

# Open in browser (if GUI available)
open tests/reports/combined_report_*.html
```
