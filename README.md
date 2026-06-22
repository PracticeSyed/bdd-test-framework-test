# 🤖 AI-Powered BDD Test Framework

Automated testing framework with API and UI (Playwright) tests.

## 📁 Project Structure

```
shared/
├── run_tests.py              # Main entry point
├── framework/                # Test framework (core files only)
│   ├── run_tests.py
│   ├── tests/
│   │   ├── api/             # API tests
│   │   ├── bdd/             # UI tests (Playwright)
│   │   └── reports/         # Combined reports
│   └── README.md
└── docs/                     # Documentation & utilities
    ├── TEST_COMMANDS.md
    ├── API_DOCS.md
    └── ... (other docs)
```

## 🚀 Quick Start

### Run All Tests (API + UI)
```bash
python run_tests.py
```

### Run Only API Tests
```bash
cd framework
behave tests/api/features
```

### Run Only UI Tests
```bash
cd framework
behave tests/bdd/features
```

## 📊 Reports

Reports are generated in:
- `framework/tests/reports/combined_report_*.html` - Combined API + UI
- `framework/tests/api/reports/` - API reports
- `framework/tests/bdd/reports/` - UI reports

## 📚 Documentation

See `docs/` folder for:
- `TEST_COMMANDS.md` - All test execution commands
- `API_DOCS.md` - API endpoint documentation
- Other guides and utilities

## ⚙️ Requirements

```bash
pip install -r framework/tests/bdd/requirements.txt
playwright install chromium
```
