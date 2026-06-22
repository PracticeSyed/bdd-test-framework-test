# 🥒 Cucumber Report Generation

## Overview
The framework automatically generates Cucumber-style JSON and HTML reports for both API and UI tests.

## Generated Reports

### Automatic Generation
When you run `python run_tests.py`, the following Cucumber reports are generated:

**API Tests:**
- `framework/tests/api/reports/cucumber_api_[timestamp].json` - Cucumber JSON
- `framework/tests/api/reports/cucumber_api_[timestamp].html` - Cucumber HTML

**UI Tests:**
- `framework/tests/bdd/reports/cucumber_ui_[timestamp].json` - Cucumber JSON
- `framework/tests/bdd/reports/cucumber_ui_[timestamp].html` - Cucumber HTML

## Manual Generation

### Generate Cucumber JSON Only
```bash
cd framework

# API tests
behave tests/api/features -f json.pretty -o tests/api/reports/cucumber_api.json

# UI tests
behave tests/bdd/features -f json.pretty -o tests/bdd/reports/cucumber_ui.json
```

### Generate HTML from JSON
```bash
cd framework
python generate_cucumber_report.py tests/api/reports/cucumber_api.json
python generate_cucumber_report.py tests/bdd/reports/cucumber_ui.json
```

## Report Features

✅ Scenario pass/fail status
✅ Step-by-step execution details
✅ Error messages for failed steps
✅ Pass rate statistics
✅ Execution timestamps
✅ Color-coded results

## View Reports

```bash
# List all Cucumber reports
ls -lt framework/tests/api/reports/cucumber_*.html
ls -lt framework/tests/bdd/reports/cucumber_*.html

# Open in browser (if GUI available)
open framework/tests/api/reports/cucumber_api_[timestamp].html
```

## Integration with CI/CD

The Cucumber JSON format is compatible with:
- Jenkins Cucumber Reports Plugin
- GitLab CI/CD
- Azure DevOps
- Allure Reports
- Cucumber Studio
