# Playwright Installation and Setup Guide

## Prerequisites
- Python 3.7 or higher
- sudo access (for system dependencies)
- Ubuntu/Debian-based Linux system

---

## Step 1: Install Playwright Python Package

```bash
pip install playwright
```

---

## Step 2: Install System Dependencies

```bash
sudo apt-get update && sudo apt-get install -y \
    libglib2.0-0t64 \
    libxcb1 \
    libx11-6 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxtst6 \
    libnspr4 \
    libnss3 \
    libatk1.0-0t64 \
    libatk-bridge2.0-0t64 \
    libxkbcommon0 \
    libxshmfence1 \
    libdbus-1-3 \
    libgbm1 \
    libdrm2 \
    libgtk-3-0t64 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libfreetype6 \
    libfontconfig1 \
    libasound2t64
```

---

## Step 3: Install Playwright Browsers

```bash
playwright install chrome
```

**Alternative browsers:**
```bash
playwright install firefox
playwright install webkit
```

---

## Step 4: Create Test Script

Create a file named `test_playwright.py`:

```python
from playwright.sync_api import sync_playwright

def test_playwright():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to a website
        page.goto('https://example.com')
        
        # Get page title
        title = page.title()
        print(f"Page title: {title}")
        
        # Verify it worked
        assert 'Example' in title
        print("✓ Playwright is working correctly!")
        
        browser.close()

if __name__ == "__main__":
    test_playwright()
```

---

## Step 5: Run the Test

```bash
python test_playwright.py
```

**Expected Output:**
```
Page title: Example Domain
✓ Playwright is working correctly!
```

---

## Common Commands

### Run script in visible mode (non-headless):
Change `headless=True` to `headless=False` in the script

### Check installed browsers:
```bash
playwright --version
```

### Reinstall browsers:
```bash
playwright install --force chromium
```

---

## Troubleshooting

### Error: "libglib-2.0.so.0: cannot open shared object file"
**Solution:** Run Step 2 again to install system dependencies

### Error: "Target page, context or browser has been closed"
**Solution:** Missing system libraries. Install all dependencies from Step 2

### Error: "playwright: command not found"
**Solution:** Reinstall playwright: `pip install --force-reinstall playwright`

### Permission denied errors:
**Solution:** Use `sudo` for system-level installations

---

## Daily Usage Workflow

1. Navigate to your project directory:
   ```bash
   cd /home/sagemaker-user/shared
   ```

2. Run your Playwright script:
   ```bash
   python your_script.py
   ```

---

## Notes

- System dependencies (Step 2) only need to be installed once
- Playwright browsers may need periodic updates: `playwright install chromium`
- Use `headless=True` for server environments without display
- Use `headless=False` for debugging and seeing browser actions

---

## Quick Reference

| Task | Command |
|------|---------|
| Install Playwright | `pip install playwright` |
| Install Chromium | `playwright install chromium` |
| Run script | `python script.py` |
| Update browsers | `playwright install --force chromium` |
| Check version | `playwright --version` |

---

**Last Updated:** 2024
**Environment:** Ubuntu 24.04 (Noble)
