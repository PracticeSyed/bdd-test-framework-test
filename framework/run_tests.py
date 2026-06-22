#!/usr/bin/env python3
"""AI-Powered BDD Test Framework"""
import sys
import json
from pathlib import Path

sys.path.insert(0, 'tests/bdd/utils')
from dom_extractor import DOMExtractor
from page_object_generator import PageObjectGenerator

class AITestFramework:
    def __init__(self, url):
        self.url = url
        self.dom_file = 'tests/bdd/config/page_objects.json'
        self.page_class_file = 'tests/bdd/pages/page_objects.py'
    
    def check_dom_changes(self):
        extractor = DOMExtractor(self.url)
        new_dom = extractor.scan_page()
        
        if Path(self.dom_file).exists():
            with open(self.dom_file, 'r') as f:
                old_dom = json.load(f)
            
            old_count = sum(len(v) for v in old_dom['elements'].values())
            new_count = sum(len(v) for v in new_dom['elements'].values())
            
            if old_count != new_count:
                print(f"⚠ DOM changed: {old_count} -> {new_count} elements")
                return True, new_dom
            print(f"✓ DOM unchanged: {new_count} elements")
            return False, old_dom
        
        return True, new_dom
    
    def update_framework(self):
        changed, dom = self.check_dom_changes()
        
        if changed:
            print("🔄 Updating page objects...")
            
            with open(self.dom_file, 'w') as f:
                json.dump(dom, f, indent=2)
            
            gen = PageObjectGenerator(self.dom_file)
            gen.save_page_class(self.page_class_file)
            
            print(f"✓ Framework updated")
        
        return changed
    
    def run_api_tests(self, timestamp):
        import subprocess
        report_dir = 'tests/api/reports'
        Path(report_dir).mkdir(parents=True, exist_ok=True)
        
        print("\n🔌 Running API Tests...")
        print("=" * 60)
        
        json_file = f'{report_dir}/cucumber_{timestamp}.json'
        result = subprocess.run([
            'behave', 'tests/api/features',
            '-f', 'json', '-o', json_file,
            '--no-capture'
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        # Fix JSON status reporting
        if Path(json_file).exists():
            subprocess.run(['python', 'fix_cucumber_json.py', json_file], capture_output=True)
        
        # Extract failed scenarios
        failed_scenarios = []
        if Path(json_file).exists():
            with open(json_file) as f:
                data = json.load(f)
                for feature in data:
                    for scenario in feature.get('elements', []):
                        if any(st.get('result', {}).get('status') == 'failed' for st in scenario.get('steps', [])):
                            failed_scenarios.append(f"API: {scenario.get('name', 'Unknown')}")
        
        return result.returncode == 0, json_file, failed_scenarios
    
    def run_ui_tests(self, timestamp):
        import subprocess
        report_dir = 'tests/bdd/reports'
        Path(report_dir).mkdir(parents=True, exist_ok=True)
        
        print("\n🖥️  Running UI Tests...")
        print("=" * 60)
        
        json_file = f'{report_dir}/cucumber_{timestamp}.json'
        result = subprocess.run([
            'behave', 'tests/bdd/features',
            '-f', 'json', '-o', json_file,
            '--no-capture'
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        # Fix JSON status reporting
        if Path(json_file).exists():
            subprocess.run(['python', 'fix_cucumber_json.py', json_file], capture_output=True)
        
        # Extract failed scenarios
        failed_scenarios = []
        if Path(json_file).exists():
            with open(json_file) as f:
                data = json.load(f)
                for feature in data:
                    for scenario in feature.get('elements', []):
                        if any(st.get('result', {}).get('status') == 'failed' for st in scenario.get('steps', [])):
                            failed_scenarios.append(f"UI: {scenario.get('name', 'Unknown')}")
        
        return result.returncode == 0, json_file, failed_scenarios
    
    def run_tests(self):
        from datetime import datetime
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Run API tests first
        api_success, api_report, api_failures = self.run_api_tests(timestamp)
        
        # Then run UI tests
        ui_success, ui_report, ui_failures = self.run_ui_tests(timestamp)
        
        # Generate combined report
        self._generate_combined_report(api_report, ui_report, timestamp)
        
        # Print failures if any
        all_failures = api_failures + ui_failures
        if all_failures:
            print("\n❌ FAILED TEST CASES:")
            for failure in all_failures:
                print(f"   • {failure}")
        else:
            print("\n✅ All tests passed!")
        
        print(f"\n📊 Report: tests/reports/combined_report_{timestamp}.html")
        
        return api_success and ui_success
    
    def _generate_combined_report(self, api_report, ui_report, timestamp):
        import json
        
        api_data = []
        ui_data = []
        
        if Path(api_report).exists():
            with open(api_report) as f:
                api_data = json.load(f)
        
        if Path(ui_report).exists():
            with open(ui_report) as f:
                ui_data = json.load(f)
        
        # Calculate stats
        def get_stats(data):
            passed = sum(1 for f in data for s in f.get('elements', []) 
                        if all(st.get('result', {}).get('status') == 'passed' for st in s.get('steps', []) if 'result' in st))
            failed = sum(1 for f in data for s in f.get('elements', []) 
                        if any(st.get('result', {}).get('status') == 'failed' for st in s.get('steps', []) if 'result' in st))
            return passed, failed
        
        api_passed, api_failed = get_stats(api_data)
        ui_passed, ui_failed = get_stats(ui_data)
        
        total_passed = api_passed + ui_passed
        total_failed = api_failed + ui_failed
        total = total_passed + total_failed
        
        # Generate HTML
        def render_scenarios(data):
            html = ''
            for f in data:
                for s in f.get('elements', []):
                    if not s.get('name'):  # Skip background/empty scenarios
                        continue
                    has_fail = any(st.get('result', {}).get('status') == 'failed' for st in s.get('steps', []) if 'result' in st)
                    status_label = '<span class="status-fail">✗ FAILED</span>' if has_fail else '<span class="status-pass">✓ PASSED</span>'
                    html += f'<div class="scenario {"fail" if has_fail else ""}"><h3>{status_label} {s.get("name", "Unknown")}</h3><p>{f.get("name", "Unknown")}</p></div>'
            return html
        
        html = f'''<!DOCTYPE html>
<html><head><title>Combined Test Report</title><style>
body{{font-family:Arial;margin:20px;background:#f5f5f5}}
.header{{background:#2196F3;color:white;padding:30px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1)}}
.header h1{{margin:0 0 10px 0;font-size:32px}}
.header p{{margin:0;opacity:0.9;font-size:14px}}
.stats{{display:flex;gap:20px;margin:30px 0;justify-content:center}}
.stat{{background:white;padding:25px;border-radius:8px;min-width:150px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.1)}}
.stat-label{{font-size:14px;color:#666;margin-bottom:10px;text-transform:uppercase;letter-spacing:1px}}
.passed{{color:#4CAF50;font-size:36px;font-weight:bold;display:block;margin:10px 0}}
.failed{{color:#f44336;font-size:36px;font-weight:bold;display:block;margin:10px 0}}
.total{{color:#2196F3;font-size:36px;font-weight:bold;display:block;margin:10px 0}}
.section{{background:white;margin:30px 0;padding:30px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1)}}
.section h2{{margin:0 0 20px 0;color:#2196F3;font-size:24px;border-bottom:2px solid #e0e0e0;padding-bottom:10px}}
.section .stats{{margin:20px 0}}
.section .stat{{min-width:120px;padding:20px}}
.scenario{{background:#f9f9f9;margin:15px 0;padding:15px 20px;border-radius:6px;border-left:5px solid #4CAF50}}
.scenario.fail{{border-left-color:#f44336;background:#fff5f5}}
.scenario h3{{margin:0 0 8px 0;font-size:16px}}
.scenario p{{margin:0;color:#666;font-size:13px}}
.status-pass{{color:#4CAF50;font-weight:bold;margin-right:8px}}
.status-fail{{color:#f44336;font-weight:bold;margin-right:8px}}
</style></head><body>
<div class="header"><h1>Cucumber Test Report</h1><p>Generated: {timestamp}</p></div>
<div class="stats">
<div class="stat"><div class="stat-label">Passed</div><div class="passed">{total_passed}</div></div>
<div class="stat"><div class="stat-label">Failed</div><div class="failed">{total_failed}</div></div>
<div class="stat"><div class="stat-label">Total</div><div class="total">{total}</div></div>
</div>
<div class="section"><h2>🔌 API Tests ({api_passed + api_failed})</h2>
<div class="stats">
<div class="stat"><div class="stat-label">Passed</div><div class="passed">{api_passed}</div></div>
<div class="stat"><div class="stat-label">Failed</div><div class="failed">{api_failed}</div></div>
</div>
{render_scenarios(api_data)}
</div>
<div class="section"><h2>🖥️ UI Tests ({ui_passed + ui_failed})</h2>
<div class="stats">
<div class="stat"><div class="stat-label">Passed</div><div class="passed">{ui_passed}</div></div>
<div class="stat"><div class="stat-label">Failed</div><div class="failed">{ui_failed}</div></div>
</div>
{render_scenarios(ui_data)}
</div>
</body></html>'''
        
        # Save combined report
        report_file = f'tests/reports/combined_report_{timestamp}.html'
        Path('tests/reports').mkdir(parents=True, exist_ok=True)
        with open(report_file, 'w') as f:
            f.write(html)
    
    def _generate_cucumber_html_reports(self, timestamp):
        import subprocess
        
        api_json = f'tests/api/reports/cucumber_api_{timestamp}.json'
        ui_json = f'tests/bdd/reports/cucumber_ui_{timestamp}.json'
        combined_html = f'tests/reports/cucumber_combined_{timestamp}.html'
        
        # Generate individual reports
        if Path(api_json).exists():
            subprocess.run(['python', 'generate_cucumber_report.py', api_json], capture_output=True)
        
        if Path(ui_json).exists():
            subprocess.run(['python', 'generate_cucumber_report.py', ui_json], capture_output=True)
        
        # Generate combined report
        if Path(api_json).exists() and Path(ui_json).exists():
            subprocess.run(['python', 'generate_combined_cucumber.py', api_json, ui_json, combined_html], capture_output=True)
        
        print(f"\n🥒 Cucumber Reports:")
        print(f"   Combined: {combined_html}")
        print(f"   API: tests/api/reports/cucumber_api_{timestamp}.html")
        print(f"   UI: tests/bdd/reports/cucumber_ui_{timestamp}.html")


if __name__ == '__main__':
    framework = AITestFramework('https://practicesoftwaretesting.com/')
    
    print("🤖 AI BDD Test Framework")
    print("=" * 60)
    
    framework.update_framework()
    
    print("\n" + "=" * 60)
    print("🧪 Running tests...")
    print("=" * 60)
    
    success = framework.run_tests()
    print("\n✓ All tests passed!" if success else "\n✗ Tests failed")
    
    # Exit with proper code for CI/CD
    sys.exit(0 if success else 1)
