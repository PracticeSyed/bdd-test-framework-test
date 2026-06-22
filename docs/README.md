# 🤖 AI-Powered BDD Test Framework

Auto-updating test framework that detects DOM changes and regenerates page objects.

## 📁 Project Structure

```
shared/
├── run_tests.py                      # Main entry point
├── tests/
│   └── bdd/
│       ├── features/                 # Gherkin feature files
│       │   ├── chrome_store.feature
│       │   └── practice_site.feature
│       ├── steps/                    # Step definitions
│       │   ├── auto_steps.py
│       │   └── chrome_store_steps.py
│       ├── pages/                    # Page object classes (auto-generated)
│       │   └── page_objects.py
│       ├── utils/                    # Framework utilities
│       │   ├── dom_extractor.py
│       │   └── page_object_generator.py
│       ├── config/                   # Configuration & DOM storage
│       │   └── page_objects.json
│       ├── reports/                  # Test reports (generated)
│       ├── environment.py            # Behave hooks
│       ├── behave.ini               # Behave configuration
│       └── requirements.txt         # Dependencies
```

## 🚀 Quick Start

### Run all tests (auto-updates DOM):
```bash
python run_tests.py
```

### Run specific feature:
```bash
behave tests/bdd/features/practice_site.feature
```

### Extract DOM only:
```bash
cd tests/bdd/utils && python dom_extractor.py
```

## 🎯 How It Works

1. **DOM Extraction** (`utils/dom_extractor.py`)
   - Scans website with Playwright
   - Extracts all interactive elements
   - Stores as JSON in `config/page_objects.json`

2. **Change Detection** (`run_tests.py`)
   - Compares current DOM with stored version
   - Detects element count changes
   - Triggers regeneration if needed

3. **Page Object Generation** (`utils/page_object_generator.py`)
   - Reads DOM JSON
   - Generates Python page object class
   - Saves to `pages/page_objects.py`

4. **BDD Testing** (`features/*.feature`)
   - Uses generated page objects
   - Runs Behave scenarios
   - Reports results

## 📝 Writing Tests

### Create a feature file:
`tests/bdd/features/my_test.feature`
```gherkin
Feature: My Test
  Scenario: Test something
    Given I open the practice software testing site
    When I interact with element "click_link_0"
    Then the page should be loaded
```

### Add step definitions:
`tests/bdd/steps/my_steps.py`
```python
from behave import given, when, then

@given('I do something')
def step_impl(context):
    # Your code here
    pass
```

## 🔄 When DOM Changes

The framework automatically:
1. ✓ Detects changes on next run
2. ✓ Updates `config/page_objects.json`
3. ✓ Regenerates `pages/page_objects.py`
4. ✓ Runs tests with new objects

## ⚙️ Configuration

### Change target URL:
Edit `run_tests.py`:
```python
framework = AITestFramework('https://your-site.com/')
```

### Add more selectors:
Edit `tests/bdd/utils/dom_extractor.py`:
```python
selectors = {
    'nav': 'nav, [role="navigation"]',
    'custom': '.your-selector',
}
```

## 📊 Reports

Test reports are generated in `tests/bdd/reports/`

## 🛠️ Maintenance

### Update dependencies:
```bash
pip install -r tests/bdd/requirements.txt
```

### Clean generated files:
```bash
rm tests/bdd/config/page_objects.json
rm tests/bdd/pages/page_objects.py
```

## ✨ Features

- 🤖 AI-powered DOM detection
- 🔄 Auto-regenerating page objects
- 📦 Clean folder structure
- 🧪 BDD with Behave
- 🎯 Zero maintenance
- 📊 Test reporting
