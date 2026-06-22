# 📊 How to View Test Reports

## ✅ Fixed: Emojis now display correctly in reports!

## Option 1: Direct File Access (Recommended)

### Copy report path and open in browser:
```bash
# Get latest report paths
ls -lt framework/tests/api/reports/cucumber_api_*.html | head -1
ls -lt framework/tests/bdd/reports/cucumber_ui_*.html | head -1
ls -lt framework/tests/reports/combined_report_*.html | head -1
```

**Then open the file path in your browser:**
- Right-click the HTML file → Open with → Browser
- Or drag and drop the file into your browser

## Option 2: HTTP Server (For Remote Access)

### Start local web server:
```bash
cd /home/sagemaker-user/shared
python view_reports.py
```

**Access reports at:**
- http://localhost:8000/tests/reports/ (Combined)
- http://localhost:8000/tests/api/reports/ (API Cucumber)
- http://localhost:8000/tests/bdd/reports/ (UI Cucumber)

## Option 3: Python HTTP Server (Quick)

```bash
cd /home/sagemaker-user/shared/framework
python -m http.server 8000
```

Then open: http://localhost:8000/tests/api/reports/

## Option 4: View in IDE

If using VS Code or similar:
1. Right-click on HTML file
2. Select "Open with Live Server" or "Open in Browser"

## Option 5: Copy to Local Machine

```bash
# Copy reports to your local machine
scp -r user@server:/home/sagemaker-user/shared/framework/tests/reports ./
```

## Latest Reports Location

**API Cucumber:**
`framework/tests/api/reports/cucumber_api_20260622_084704.html`

**UI Cucumber:**
`framework/tests/bdd/reports/cucumber_ui_20260622_084704.html`

**Combined:**
`framework/tests/reports/combined_report_20260622_084704.html`

## Quick View Command

```bash
# List all reports with timestamps
find framework/tests -name "*.html" -type f -exec ls -lh {} \; | sort -k6,7
```
