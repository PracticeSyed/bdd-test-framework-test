#!/usr/bin/env python3
"""Fix Cucumber JSON to show correct scenario statuses"""
import json
import sys

def fix_cucumber_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    for feature in data:
        # Recalculate feature status based on scenarios
        has_failed = False
        has_passed = False
        
        for scenario in feature.get('elements', []):
            # Calculate scenario status from steps
            scenario_failed = any(
                step.get('result', {}).get('status') == 'failed' 
                for step in scenario.get('steps', [])
            )
            
            if scenario_failed:
                scenario['status'] = 'failed'
                has_failed = True
            else:
                scenario['status'] = 'passed'
                has_passed = True
        
        # Set feature status: failed if ANY scenario failed, else passed
        feature['status'] = 'failed' if has_failed else 'passed'
    
    # Save fixed JSON
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Fixed: {json_file}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python fix_cucumber_json.py <json_file>")
        sys.exit(1)
    
    fix_cucumber_json(sys.argv[1])
