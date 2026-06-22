#!/usr/bin/env python3
"""View Cucumber reports in terminal"""
import json
import sys
from pathlib import Path

def view_cucumber_report(json_file):
    with open(json_file) as f:
        data = json.load(f)
    
    # Calculate stats
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
    
    # Print report
    print("\n" + "="*80)
    print("🥒 CUCUMBER TEST REPORT")
    print("="*80)
    print(f"\n📊 SUMMARY:")
    print(f"   Scenarios: {total_scenarios} total | ✅ {passed_scenarios} passed | ❌ {failed_scenarios} failed")
    print(f"   Steps:     {total_steps} total | ✅ {passed_steps} passed | ❌ {failed_steps} failed")
    print(f"   Pass Rate: {int(passed_scenarios/total_scenarios*100) if total_scenarios > 0 else 0}%")
    
    # Print features
    for feature in data:
        feature_name = feature.get('name', 'Unknown Feature')
        print(f"\n{'='*80}")
        print(f"📋 {feature_name}")
        print(f"{'='*80}")
        
        for scenario in feature.get('elements', []):
            scenario_name = scenario.get('name', 'Unknown Scenario')
            scenario_failed = any(s.get('result', {}).get('status') == 'failed' for s in scenario.get('steps', []))
            
            status_icon = "❌" if scenario_failed else "✅"
            print(f"\n  {status_icon} Scenario: {scenario_name}")
            
            for step in scenario.get('steps', []):
                keyword = step.get('keyword', '')
                name = step.get('name', '')
                status = step.get('result', {}).get('status', 'undefined')
                
                if status == 'passed':
                    icon = "  ✓"
                elif status == 'failed':
                    icon = "  ✗"
                else:
                    icon = "  ○"
                
                print(f"    {icon} {keyword}{name}")
                
                if status == 'failed' and 'result' in step and 'error_message' in step['result']:
                    error = step['result']['error_message']
                    print(f"       ERROR: {error[:200]}")
    
    print("\n" + "="*80 + "\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        # Find latest reports
        api_reports = sorted(Path('tests/api/reports').glob('cucumber_*.json'), reverse=True)
        ui_reports = sorted(Path('tests/bdd/reports').glob('cucumber_*.json'), reverse=True)
        
        if api_reports:
            print("\n🔌 API TEST REPORT:")
            view_cucumber_report(api_reports[0])
        
        if ui_reports:
            print("\n🖥️  UI TEST REPORT:")
            view_cucumber_report(ui_reports[0])
    else:
        view_cucumber_report(sys.argv[1])
