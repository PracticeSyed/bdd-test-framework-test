#!/usr/bin/env python3
"""
AI-Powered Context Test Runner
Usage: python ai_test_runner.py "Test login as admin user with valid credentials"
"""

import sys
import json
import subprocess
from pathlib import Path

class AITestRunner:
    def __init__(self):
        self.context_file = Path(__file__).parent / 'tests/bdd/context/app_context.json'
        self.load_context()
    
    def load_context(self):
        with open(self.context_file, 'r') as f:
            self.context = json.load(f)
    
    def parse_prompt(self, prompt):
        """Parse natural language prompt into test parameters"""
        prompt_lower = prompt.lower()
        
        # Detect persona
        persona = None
        for p in self.context['user_personas']:
            if p['name'].lower() in prompt_lower:
                persona = p['name']
                break
        
        # Detect flow
        flow = None
        for f in self.context['critical_flows']:
            if any(word in prompt_lower for word in f['name'].lower().split()):
                flow = f['name']
                break
        
        # Detect business rules
        rules = [r for r in self.context['business_rules'] 
                if any(word in prompt_lower for word in r.lower().split())]
        
        return {
            'persona': persona,
            'flow': flow,
            'rules': rules,
            'prompt': prompt
        }
    
    def generate_feature(self, parsed):
        """Generate Gherkin feature from parsed prompt"""
        feature = f"""Feature: {parsed['prompt']}

  Background:
    Given the application context is loaded
    And business rules are defined
"""
        
        if parsed['persona']:
            feature += f"""
  Scenario: {parsed['prompt']}
    Given I am a "{parsed['persona']}"
"""
        
        if parsed['flow'] == 'Product Purchase Flow':
            feature += """    And I am logged in with valid credentials
    When I browse products
    And I add a product to cart
    And I proceed to checkout
    Then the order total should respect business rules
    And I should see payment options
"""
        
        if any('shipping' in r.lower() for r in parsed['rules']):
            feature += """
  Scenario: Validate shipping rules
    Given I am a "Registered User"
    And I have items in cart totaling "$55"
    When I view cart summary
    Then shipping cost should be "$0"
"""
        
        return feature
    
    def run_test(self, prompt):
        """Main entry point"""
        print(f"\n🤖 AI Test Runner")
        print("=" * 60)
        print(f"📝 Prompt: {prompt}\n")
        
        parsed = self.parse_prompt(prompt)
        
        print("🔍 Detected Context:")
        print(f"   Persona: {parsed['persona'] or 'None'}")
        print(f"   Flow: {parsed['flow'] or 'None'}")
        print(f"   Rules: {len(parsed['rules'])} matched\n")
        
        # Generate feature file
        feature_content = self.generate_feature(parsed)
        feature_path = Path(__file__).parent / 'tests/bdd/features/ai_generated.feature'
        
        with open(feature_path, 'w') as f:
            f.write(feature_content)
        
        print("✓ Generated feature file\n")
        print("=" * 60)
        print("🧪 Running Tests...\n")
        
        # Run behave
        result = subprocess.run(
            ['behave', 'features/ai_generated.feature'],
            cwd=Path(__file__).parent / 'tests/bdd',
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        return result.returncode == 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python ai_test_runner.py 'Your test prompt here'")
        print("\nExamples:")
        print("  python ai_test_runner.py 'Test guest user browsing products'")
        print("  python ai_test_runner.py 'Validate registered user purchase flow'")
        print("  python ai_test_runner.py 'Check free shipping rules'")
        sys.exit(1)
    
    prompt = ' '.join(sys.argv[1:])
    runner = AITestRunner()
    success = runner.run_test(prompt)
    sys.exit(0 if success else 1)
