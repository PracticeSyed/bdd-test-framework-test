# 🎭 Playwright BDD Test Framework - Complete Guide

## 📋 Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Framework Architecture](#framework-architecture)
5. [Step-by-Step Setup](#step-by-step-setup)
6. [Running Tests](#running-tests)
7. [Writing Your First Test](#writing-your-first-test)
8. [Advanced Usage](#advanced-usage)
9. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

This is an **AI-powered BDD test framework** that:
- ✅ Automatically detects DOM changes on websites
- ✅ Regenerates page objects when UI changes
- ✅ Uses Playwright for browser automation
- ✅ Implements BDD with Behave (Gherkin syntax)
- ✅ Requires zero maintenance for UI updates

---

## 📦 Prerequisites

Before starting, ensure you have:

```bash
# Python 3.8 or higher
python --version

# pip (Python package manager)
pip --version

# Node.js (for Playwright)
node --version
npm --version
```

---

## 🔧 Installation

### Step 1: Install Python Dependencies

```bash
cd shared/tests/bdd
pip install -r requirements.txt
```

**What gets installed:**
- `playwright` - Browser automation
- `behave` - BDD framework
- `pytest` - Testing utilities

### Step 2: Install Playwright Browsers

```bash
playwright install
```

This downloads Chromium, Firefox, and WebKit browsers.

### Step 3: Verify Installation

```bash
python -c "from playwright.sync_api import sync_playwright; print('✓ Playwright ready')"
```

---

## 🏗️ Framework Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    run_tests.py                         │
│              (Main Orchestrator)                        │
└────────────┬────────────────────────────────────────────┘
             │
             ├──► 1. DOM Extraction (dom_extractor.py)
             │    └─► Scans website → page_objects.json
             │
             ├──► 2. Change Detection
             │    └─► Compares old vs new DOM
             │
             ├──► 3. Page Object Generation (page_object_generator.py)
             │    └─► Generates page_objects.py
             │
             └──► 4. Test Execution (Behave)
                  └─► Runs .feature files → Reports
```

### Key Components:

| Component | Purpose | Location |
|-----------|---------|----------|
| **DOM Extractor** | Scans website, extracts elements | `utils/dom_extractor.py` |
| **Page Object Generator** | Creates Python classes from DOM | `utils/page_object_generator.py` |
| **Feature Files** | Gherkin test scenarios | `features/*.feature` |
| **Step Definitions** | Python implementation of steps | `steps/*.py` |
| **Page Objects** | Auto-generated element locators | `pages/page_objects.py` |
| **Config** | Stored DOM structure | `config/page_objects.json` |

---

## 🚀 Step-by-Step Setup

### Step 1: Navigate to Project Root

```bash
cd /home/sagemaker-user/shared
```

### Step 2: First-Time DOM Extraction

```bash
# Extract DOM from target website
cd tests/bdd/utils
python dom_extractor.py
```

**What happens:**
1. Playwright opens browser
2. Navigates to target URL
3. Extracts all interactive elements (buttons, links, inputs)
4. Saves to `config/page_objects.json`

### Step 3: Generate Page Objects

```bash
cd ..
python utils/page_object_generator.py
```

**Output:** Creates `pages/page_objects.py` with element locators

### Step 4: Run Your First Test

```bash
cd /home/sagemaker-user/shared
python run_tests.py
```

---

## 🎮 Running Tests

### Method 1: Automated (Recommended)

```bash
# From project root
python run_tests.py
```

**This automatically:**
- ✓ Checks for DOM changes
- ✓ Updates page objects if needed
- ✓ Runs all tests
- ✓ Generates reports

### Method 2: Run Specific Feature

```bash
cd tests/bdd
behave features/practice_site.feature
```

### Method 3: Run with Tags

```bash
behave --tags=@smoke
behave --tags=@regression
```

### Method 4: Run Single Scenario

```bash
behave features/practice_site.feature:10  # Line number
```

### Method 5: Headless Mode

```bash
behave -D headless=true
```

---

## ✍️ Writing Your First Test

### Step 1: Create Feature File

`tests/bdd/features/login.feature`

```gherkin
Feature: User Login
  As a user
  I want to log into the application
  So that I can access my account

  @smoke
  Scenario: Successful login
    Given I open the practice software testing site
    When I click on element "login_button"
    And I enter "user@example.com" into "email_input"
    And I enter "password123" into "password_input"
    And I click on element "submit_button"
    Then I should see element "dashboard"

  @negative
  Scenario: Failed login with invalid credentials
    Given I open the practice software testing site
    When I enter "wrong@email.com" into "email_input"
    And I enter "wrongpass" into "password_input"
    And I click on element "submit_button"
    Then I should see element "error_message"
```

### Step 2: Create Step Definitions

`tests/bdd/steps/login_steps.py`

```python
from behave import given, when, then
from playwright.sync_api import expect

@given('I open the practice software testing site')
def open_site(context):
    context.page.goto('https://practice.expandtesting.com/login')
    context.page.wait_for_load_state('networkidle')

@when('I click on element "{element_name}"')
def click_element(context, element_name):
    page_obj = context.page_objects
    locator = getattr(page_obj, element_name)
    context.page.locator(locator).click()

@when('I enter "{text}" into "{element_name}"')
def enter_text(context, text, element_name):
    page_obj = context.page_objects
    locator = getattr(page_obj, element_name)
    context.page.locator(locator).fill(text)

@then('I should see element "{element_name}"')
def verify_element(context, element_name):
    page_obj = context.page_objects
    locator = getattr(page_obj, element_name)
    expect(context.page.locator(locator)).to_be_visible()
```

### Step 3: Run Your Test

```bash
cd /home/sagemaker-user/shared
python run_tests.py
```

---

## 🔥 Advanced Usage

### Custom DOM Extraction

Edit `tests/bdd/utils/dom_extractor.py`:

```python
selectors = {
    'buttons': 'button, [role="button"], input[type="submit"]',
    'links': 'a[href]',
    'inputs': 'input, textarea, select',
    'forms': 'form',
    'modals': '[role="dialog"], .modal',
    'custom': '.your-custom-selector',  # Add your own
}
```

### Change Target URL

Edit `run_tests.py`:

```python
# Change this line
framework = AITestFramework('https://your-website.com/')
```

### Parallel Execution

```bash
behave --processes 4 --parallel-element feature
```

### Generate HTML Report

```bash
behave -f html -o tests/bdd/reports/report.html
```

### Debug Mode

```bash
behave --no-capture --no-capture-stderr
```

---

## 🎭 Playwright-Specific Commands

### Browser Context

```python
# In your step definitions
@given('I open browser in mobile view')
def mobile_view(context):
    context.page.set_viewport_size({"width": 375, "height": 667})

@when('I take a screenshot')
def screenshot(context):
    context.page.screenshot(path='tests/bdd/reports/screenshot.png')
```

### Waiting Strategies

```python
# Wait for element
context.page.wait_for_selector('#element-id', timeout=5000)

# Wait for navigation
context.page.wait_for_url('**/dashboard')

# Wait for network idle
context.page.wait_for_load_state('networkidle')
```

### Assertions

```python
from playwright.sync_api import expect

# Visibility
expect(context.page.locator('#element')).to_be_visible()

# Text content
expect(context.page.locator('h1')).to_have_text('Welcome')

# Count
expect(context.page.locator('.item')).to_have_count(5)
```

---

## 🐛 Troubleshooting

### Issue 1: Playwright Not Found

```bash
# Solution
pip install playwright
playwright install
```

### Issue 2: Browser Launch Failed

```bash
# Install system dependencies (Linux)
playwright install-deps
```

### Issue 3: Element Not Found

```bash
# Re-extract DOM
cd tests/bdd/utils
python dom_extractor.py
cd ..
python utils/page_object_generator.py
```

### Issue 4: Tests Fail After UI Change

```bash
# Framework auto-fixes this, just run:
python run_tests.py
```

### Issue 5: Permission Denied

```bash
chmod +x run_tests.py
chmod +x run-mcp.sh
```

---

## 📊 Understanding Reports

After running tests, check:

```
tests/bdd/reports/
├── report.html          # HTML test report
├── screenshots/         # Failure screenshots
└── logs/               # Execution logs
```

---

## 🔄 Workflow Summary

```
1. Write .feature file (Gherkin)
   ↓
2. Write step definitions (.py)
   ↓
3. Run: python run_tests.py
   ↓
4. Framework extracts DOM automatically
   ↓
5. Generates page objects
   ↓
6. Executes tests
   ↓
7. View reports
```

---

## 📚 Quick Reference

| Task | Command |
|------|---------|
| Run all tests | `python run_tests.py` |
| Run specific feature | `behave features/file.feature` |
| Extract DOM | `cd tests/bdd/utils && python dom_extractor.py` |
| Generate page objects | `python tests/bdd/utils/page_object_generator.py` |
| View report | Open `tests/bdd/reports/report.html` |
| Debug test | `behave --no-capture` |
| Run with tags | `behave --tags=@smoke` |

---

## 🎓 Best Practices

1. **Use descriptive scenario names**
2. **Tag tests** (@smoke, @regression, @critical)
3. **Keep steps reusable**
4. **One assertion per Then step**
5. **Use Background for common steps**
6. **Run tests in CI/CD pipeline**
7. **Review reports after each run**

---

## 🚀 Next Steps

1. ✅ Install dependencies
2. ✅ Run `python run_tests.py`
3. ✅ Write your first feature file
4. ✅ Add custom step definitions
5. ✅ Integrate with CI/CD

---

**Need Help?** Check the main README.md or review example tests in `tests/bdd/features/`
