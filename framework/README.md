# Test Framework

## Structure
```
framework/
├── run_tests.py           # Main test runner
├── tests/
│   ├── api/              # API tests
│   │   ├── features/
│   │   ├── steps/
│   │   ├── reports/
│   │   ├── behave.ini
│   │   └── environment.py
│   ├── bdd/              # UI tests (Playwright)
│   │   ├── features/
│   │   ├── steps/
│   │   ├── pages/
│   │   ├── utils/
│   │   ├── config/
│   │   ├── context/
│   │   ├── reports/
│   │   ├── behave.ini
│   │   ├── environment.py
│   │   └── requirements.txt
│   └── reports/          # Combined reports
```

## Run Tests
```bash
# From project root
python run_tests.py

# From framework folder
cd framework
python run_tests.py
```
