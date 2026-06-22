from playwright.sync_api import sync_playwright
import json
from datetime import datetime

class DOMExtractor:
    def __init__(self, url):
        self.url = url
        self.dom_map = {}
        
    def extract_element(self, element):
        """Extract element details recursively"""
        try:
            tag = element.evaluate('el => el.tagName.toLowerCase()')
            text = element.inner_text()[:100] if element.is_visible() else ''
            attrs = element.evaluate('el => { const a = {}; for (let attr of el.attributes) a[attr.name] = attr.value; return a; }')
            selector = element.evaluate('el => el.id ? "#" + el.id : el.className ? el.tagName.toLowerCase() + "." + el.className.split(" ")[0] : el.tagName.toLowerCase()')
            return {'tag': tag, 'text': text, 'attributes': attrs, 'selector': selector}
        except:
            return None
    
    def scan_page(self):
        """Scan page and extract DOM structure"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.url, wait_until='domcontentloaded', timeout=60000)
            
            # Extract key elements
            self.dom_map = {
                'url': self.url,
                'title': page.title(),
                'timestamp': datetime.now().isoformat(),
                'elements': {}
            }
            
            # Common selectors to extract
            selectors = {
                'nav': 'nav, [role="navigation"]',
                'header': 'header, [role="banner"]',
                'main': 'main, [role="main"]',
                'footer': 'footer, [role="contentinfo"]',
                'buttons': 'button, [role="button"]',
                'links': 'a[href]',
                'forms': 'form',
                'inputs': 'input, textarea, select'
            }
            
            for name, selector in selectors.items():
                elements = page.locator(selector).all()
                self.dom_map['elements'][name] = []
                for el in elements[:10]:  # Limit to first 10
                    data = self.extract_element(el)
                    if data:
                        self.dom_map['elements'][name].append(data)
            
            browser.close()
        
        return self.dom_map
    
    def save(self, filename='page_objects.json'):
        """Save DOM map to file"""
        with open(filename, 'w') as f:
            json.dump(self.dom_map, f, indent=2)
        return filename
    
    def load(self, filename='page_objects.json'):
        """Load existing DOM map"""
        with open(filename, 'r') as f:
            self.dom_map = json.load(f)
        return self.dom_map

if __name__ == '__main__':
    extractor = DOMExtractor('https://practicesoftwaretesting.com/')
    dom = extractor.scan_page()
    file = extractor.save()
    print(f"✓ DOM extracted and saved to {file}")
    print(f"✓ Found {sum(len(v) for v in dom['elements'].values())} elements")
