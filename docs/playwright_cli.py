#!/usr/bin/env python3
"""
Playwright Framework CLI - Natural Language Automation
Usage: python playwright_cli.py "run playwright framework"
"""
import sys
import subprocess
import json
from pathlib import Path

sys.path.insert(0, 'tests/bdd/utils')
from dom_extractor import DOMExtractor
from page_object_generator import PageObjectGenerator

class PlaywrightFrameworkCLI:
    def __init__(self):
        self.commands = {
            'run': self.run_framework,
            'extract': self.extract_dom,
            'generate': self.generate_page_objects,
            'test': self.run_tests,
            'update': self.update_framework,
            'setup': self.setup_framework,
            'status': self.show_status,
            'help': self.show_help
        }
        
    def parse_command(self, prompt):
        """Parse natural language prompt"""
        prompt = prompt.lower()
        
        # Map natural language to commands
        if any(x in prompt for x in ['run', 'execute', 'start']):
            if 'framework' in prompt or 'playwright' in prompt:
                return 'run'
        if 'extract' in prompt or 'scan' in prompt or 'dom' in prompt:
            return 'extract'
        if 'generate' in prompt or 'create page' in prompt:
            return 'generate'
        if 'test' in prompt or 'behave' in prompt:
            return 'test'
        if 'update' in prompt or 'refresh' in prompt:
            return 'update'
        if 'setup' in prompt or 'install' in prompt:
            return 'setup'
        if 'status' in prompt or 'info' in prompt:
            return 'status'
        
        return 'help'
    
    def run_framework(self):
        """Run complete framework: extract → generate → test"""
        print("🤖 Running Playwright Framework")
        print("=" * 60)
        
        print("\n📊 Step 1/4: Checking DOM changes...")
        changed = self.update_framework()
        
        print("\n📊 Step 2/4: Validating page objects...")
        if Path('tests/bdd/pages/page_objects.py').exists():
            print("✓ Page objects ready")
        else:
            print("⚠ Generating page objects...")
            self.generate_page_objects()
        
        print("\n📊 Step 3/4: Running BDD tests...")
        success = self.run_tests()
        
        print("\n📊 Step 4/4: Complete!")
        if success:
            print("✓ All tests passed!")
        else:
            print("✗ Some tests failed")
        
        return success
    
    def extract_dom(self):
        """Extract DOM structure from website"""
        print("🔍 Extracting DOM structure...")
        
        url = 'https://practicesoftwaretesting.com/'
        extractor = DOMExtractor(url)
        dom = extractor.scan_page()
        
        file = 'tests/bdd/config/page_objects.json'
        with open(file, 'w') as f:
            json.dump(dom, f, indent=2)
        
        count = sum(len(v) for v in dom['elements'].values())
        print(f"✓ Extracted {count} elements")
        print(f"✓ Saved to {file}")
        
        return True
    
    def generate_page_objects(self):
        """Generate page object classes"""
        print("⚙️ Generating page objects...")
        
        gen = PageObjectGenerator('tests/bdd/config/page_objects.json')
        file = gen.save_page_class('tests/bdd/pages/page_objects.py')
        
        print(f"✓ Generated {file}")
        return True
    
    def run_tests(self):
        """Run BDD tests"""
        print("🧪 Running tests...")
        
        result = subprocess.run(
            ['behave', 'tests/bdd/features'],
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        return result.returncode == 0
    
    def update_framework(self):
        """Check and update if DOM changed"""
        dom_file = 'tests/bdd/config/page_objects.json'
        
        extractor = DOMExtractor('https://practicesoftwaretesting.com/')
        new_dom = extractor.scan_page()
        
        if Path(dom_file).exists():
            with open(dom_file, 'r') as f:
                old_dom = json.load(f)
            
            old_count = sum(len(v) for v in old_dom['elements'].values())
            new_count = sum(len(v) for v in new_dom['elements'].values())
            
            if old_count != new_count:
                print(f"⚠ DOM changed: {old_count} → {new_count} elements")
                
                with open(dom_file, 'w') as f:
                    json.dump(new_dom, f, indent=2)
                
                gen = PageObjectGenerator(dom_file)
                gen.save_page_class('tests/bdd/pages/page_objects.py')
                
                print("✓ Framework updated")
                return True
            else:
                print(f"✓ DOM unchanged: {new_count} elements")
                return False
        else:
            with open(dom_file, 'w') as f:
                json.dump(new_dom, f, indent=2)
            
            gen = PageObjectGenerator(dom_file)
            gen.save_page_class('tests/bdd/pages/page_objects.py')
            
            print("✓ Framework initialized")
            return True
    
    def setup_framework(self):
        """Setup framework dependencies"""
        print("📦 Setting up framework...")
        
        subprocess.run(['pip', 'install', '-q', '-r', 'tests/bdd/requirements.txt'])
        subprocess.run(['playwright', 'install', 'chromium'])
        
        print("✓ Dependencies installed")
        return True
    
    def show_status(self):
        """Show framework status"""
        print("📊 Framework Status")
        print("=" * 60)
        
        dom_file = Path('tests/bdd/config/page_objects.json')
        page_file = Path('tests/bdd/pages/page_objects.py')
        
        if dom_file.exists():
            with open(dom_file, 'r') as f:
                dom = json.load(f)
            count = sum(len(v) for v in dom['elements'].values())
            print(f"✓ DOM: {count} elements extracted")
            print(f"  URL: {dom['url']}")
            print(f"  Last scan: {dom['timestamp']}")
        else:
            print("✗ DOM: Not extracted yet")
        
        if page_file.exists():
            print(f"✓ Page Objects: Generated")
        else:
            print("✗ Page Objects: Not generated yet")
        
        features = list(Path('tests/bdd/features').glob('*.feature'))
        print(f"✓ Features: {len(features)} test files")
        
        return True
    
    def show_help(self):
        """Show help message"""
        print("""
🤖 Playwright Framework CLI - Natural Language Commands

USAGE:
  python playwright_cli.py "your command"

COMMANDS:
  "run playwright framework"     → Run complete framework
  "extract dom"                  → Extract DOM structure only
  "generate page objects"        → Generate page objects only
  "run tests"                    → Run BDD tests only
  "update framework"             → Check and update DOM
  "setup framework"              → Install dependencies
  "show status"                  → Show framework status
  "help"                         → Show this help

EXAMPLES:
  python playwright_cli.py "run playwright framework"
  python playwright_cli.py "extract dom from website"
  python playwright_cli.py "run tests"
  python playwright_cli.py "show status"

SHORTCUTS:
  python playwright_cli.py run
  python playwright_cli.py test
  python playwright_cli.py status
        """)
        return True
    
    def execute(self, prompt):
        """Execute command from prompt"""
        command = self.parse_command(prompt)
        
        if command in self.commands:
            return self.commands[command]()
        else:
            print(f"❌ Unknown command: {prompt}")
            self.show_help()
            return False

def main():
    cli = PlaywrightFrameworkCLI()
    
    if len(sys.argv) < 2:
        print("Usage: python playwright_cli.py \"run playwright framework\"")
        cli.show_help()
        sys.exit(1)
    
    prompt = ' '.join(sys.argv[1:])
    success = cli.execute(prompt)
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
