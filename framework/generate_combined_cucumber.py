#!/usr/bin/env python3
"""Generate Combined Cucumber HTML report from API and UI JSON"""
import json
import sys
from pathlib import Path
from datetime import datetime

def generate_combined_cucumber_report(api_json, ui_json, output_file):
    api_data = []
    ui_data = []
    
    if Path(api_json).exists():
        with open(api_json) as f:
            api_data = json.load(f)
    
    if Path(ui_json).exists():
        with open(ui_json) as f:
            ui_data = json.load(f)
    
    # Calculate stats
    def get_stats(data):
        total_scenarios = 0
        passed_scenarios = 0
        failed_scenarios = 0
        total_steps = 0
        passed_steps = 0
        failed_steps = 0
        
        for feature in data:
            for scenario in feature.get('elements', []):
                total_scenarios += 1
                scenario_passed = True
                for step in scenario.get('steps', []):
                    total_steps += 1
                    status = step.get('result', {}).get('status', 'undefined')
                    if status == 'passed':
                        passed_steps += 1
                    elif status == 'failed':
                        failed_steps += 1
                        scenario_passed = False
                
                if scenario_passed:
                    passed_scenarios += 1
                else:
                    failed_scenarios += 1
        
        return total_scenarios, passed_scenarios, failed_scenarios, total_steps, passed_steps, failed_steps
    
    api_stats = get_stats(api_data)
    ui_stats = get_stats(ui_data)
    
    total_scenarios = api_stats[0] + ui_stats[0]
    passed_scenarios = api_stats[1] + ui_stats[1]
    failed_scenarios = api_stats[2] + ui_stats[2]
    total_steps = api_stats[3] + ui_stats[3]
    passed_steps = api_stats[4] + ui_stats[4]
    failed_steps = api_stats[5] + ui_stats[5]
    
    # Generate HTML
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Combined Cucumber Test Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }}
        .header {{ background: #00a818; color: white; padding: 20px; border-radius: 5px; }}
        .stats {{ display: flex; gap: 20px; margin: 20px 0; }}
        .stat {{ background: white; padding: 20px; border-radius: 5px; flex: 1; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .stat-value {{ font-size: 32px; font-weight: bold; margin: 10px 0; }}
        .passed {{ color: #00a818; }}
        .failed {{ color: #d9534f; }}
        .section {{ background: white; margin: 20px 0; padding: 20px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .section-title {{ font-size: 24px; font-weight: bold; color: #00a818; margin-bottom: 20px; border-bottom: 2px solid #00a818; padding-bottom: 10px; }}
        .feature {{ margin: 20px 0; padding: 15px; background: #f9f9f9; border-radius: 5px; }}
        .feature-name {{ font-size: 18px; font-weight: bold; color: #333; margin-bottom: 15px; }}
        .scenario {{ margin: 15px 0; padding: 15px; background: white; border-radius: 5px; border-left: 4px solid #00a818; }}
        .scenario.failed {{ border-left-color: #d9534f; }}
        .scenario-name {{ font-weight: bold; margin-bottom: 10px; color: #555; }}
        .step {{ padding: 8px; margin: 5px 0; font-family: monospace; font-size: 14px; }}
        .step.passed {{ color: #00a818; }}
        .step.failed {{ color: #d9534f; background: #ffe6e6; border-radius: 3px; padding: 10px; }}
        .step.undefined {{ color: #999; }}
        .error {{ background: #ffe6e6; padding: 10px; margin: 10px 0; border-radius: 3px; font-family: monospace; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>&#x1F952; Combined Cucumber Test Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="stats">
        <div class="stat">
            <div>Total Scenarios</div>
            <div class="stat-value">{total_scenarios}</div>
            <div><span class="passed">{passed_scenarios} passed</span> / <span class="failed">{failed_scenarios} failed</span></div>
        </div>
        <div class="stat">
            <div>Total Steps</div>
            <div class="stat-value">{total_steps}</div>
            <div><span class="passed">{passed_steps} passed</span> / <span class="failed">{failed_steps} failed</span></div>
        </div>
        <div class="stat">
            <div>Pass Rate</div>
            <div class="stat-value passed">{int(passed_scenarios/total_scenarios*100) if total_scenarios > 0 else 0}%</div>
        </div>
    </div>
'''
    
    # Add API section
    if api_data:
        html += f'<div class="section"><div class="section-title">&#x1F50C; API Tests ({api_stats[0]} scenarios, {api_stats[3]} steps)</div>'
        for feature in api_data:
            feature_name = feature.get('name', 'Unknown Feature')
            html += f'<div class="feature"><div class="feature-name">&#x1F4CB; {feature_name}</div>'
            
            for scenario in feature.get('elements', []):
                scenario_name = scenario.get('name', 'Unknown Scenario')
                scenario_failed = any(s.get('result', {}).get('status') == 'failed' for s in scenario.get('steps', []))
                
                html += f'<div class="scenario {"failed" if scenario_failed else ""}"><div class="scenario-name">&#x2022; {scenario_name}</div>'
                
                for step in scenario.get('steps', []):
                    keyword = step.get('keyword', '')
                    name = step.get('name', '')
                    status = step.get('result', {}).get('status', 'undefined')
                    
                    html += f'<div class="step {status}">{keyword} {name}</div>'
                    
                    if status == 'failed' and 'result' in step and 'error_message' in step['result']:
                        error = step['result']['error_message']
                        html += f'<div class="error">{error[:500]}</div>'
                
                html += '</div>'
            
            html += '</div>'
        html += '</div>'
    
    # Add UI section
    if ui_data:
        html += f'<div class="section"><div class="section-title">&#x1F5A5; UI Tests ({ui_stats[0]} scenarios, {ui_stats[3]} steps)</div>'
        for feature in ui_data:
            feature_name = feature.get('name', 'Unknown Feature')
            html += f'<div class="feature"><div class="feature-name">&#x1F4CB; {feature_name}</div>'
            
            for scenario in feature.get('elements', []):
                scenario_name = scenario.get('name', 'Unknown Scenario')
                scenario_failed = any(s.get('result', {}).get('status') == 'failed' for s in scenario.get('steps', []))
                
                html += f'<div class="scenario {"failed" if scenario_failed else ""}"><div class="scenario-name">&#x2022; {scenario_name}</div>'
                
                for step in scenario.get('steps', []):
                    keyword = step.get('keyword', '')
                    name = step.get('name', '')
                    status = step.get('result', {}).get('status', 'undefined')
                    
                    html += f'<div class="step {status}">{keyword} {name}</div>'
                    
                    if status == 'failed' and 'result' in step and 'error_message' in step['result']:
                        error = step['result']['error_message']
                        html += f'<div class="error">{error[:500]}</div>'
                
                html += '</div>'
            
            html += '</div>'
        html += '</div>'
    
    html += '</body></html>'
    
    with open(output_file, 'w', encoding='utf-8', errors='replace') as f:
        f.write(html)
    
    print(f"✓ Combined Cucumber report generated: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python generate_combined_cucumber.py <api_json> <ui_json> <output_html>")
        sys.exit(1)
    
    generate_combined_cucumber_report(sys.argv[1], sys.argv[2], sys.argv[3])
