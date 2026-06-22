# AI-Powered BDD Test Framework

## 🤖 What This Does

This framework **automatically detects DOM changes** and regenerates page objects - making your tests self-maintaining when developers update the website.

## 📁 Framework Structure

```
shared/
├── ai_test_framework.py          # Main orchestrator (run this)
├── dom_extractor.py               # Extracts DOM structure
├── page_object_generator.py      # Generates page objects from DOM
├── page_objects.json              # Stored DOM structure (auto-updated)
├── page_objects.py                # Generated page object class (auto-updated)
└── features/
    ├── practice_site.feature      # BDD scenarios
    └── steps/
        └── auto_steps.py          # BDD step definitions
```

## 🚀 Usage

### Run the framework (auto-updates DOM if changed):
```bash
python ai_test_framework.py
```

### Manual DOM extraction:
```bash
python dom_extractor.py
```

### Manual page object generation:
```bash
python page_object_generator.py
```

### Run BDD tests only:
```bash
behave features/practice_site.feature
```

## 🎯 How It Works

1. **DOM Extraction**: Scans the website and extracts all interactive elements
2. **Change Detection**: Compares with previous scan to detect updates
3. **Auto-Generation**: Regenerates page object classes if DOM changed
4. **BDD Integration**: Uses generated objects in Behave tests

## 📝 Example: Adding New Tests

Edit `features/practice_site.feature`:
```gherkin
Scenario: Click a link
  Given I open the practice software testing site
  When I interact with element "click_link_0"
  Then the page should be loaded
```

The framework automatically:
- ✓ Detects new elements on the page
- ✓ Generates methods for them
- ✓ Makes them available in your tests

## 🔄 When Developer Updates DOM

Just run:
```bash
python ai_test_framework.py
```

The framework will:
1. Detect the changes
2. Update `page_objects.json`
3. Regenerate `page_objects.py`
4. Run your tests with new objects

## 🎨 Customization

### Add more selectors to extract:
Edit `dom_extractor.py` line 38:
```python
selectors = {
    'nav': 'nav, [role="navigation"]',
    'custom': '.my-custom-selector',  # Add your own
}
```

### Change URL:
```python
framework = AITestFramework('https://your-site.com/')
```

## ✨ Key Features

- 🤖 **AI-Powered**: Auto-detects DOM changes
- 🔄 **Self-Updating**: Regenerates page objects automatically
- 📦 **Reusable**: Stores DOM as JSON for reuse
- 🧪 **BDD Ready**: Integrates with Behave framework
- 🎯 **Zero Maintenance**: No manual page object updates needed
