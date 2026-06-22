import json
from pathlib import Path

class PageObjectGenerator:
    def __init__(self, dom_file='page_objects.json'):
        self.dom_file = dom_file
        self.load_dom()
    
    def load_dom(self):
        """Load DOM structure"""
        with open(self.dom_file, 'r') as f:
            self.dom = json.load(f)
    
    def generate_page_class(self):
        """Generate Python page object class from DOM"""
        class_name = self.dom['url'].split('//')[1].split('/')[0].replace('.', '_').title() + 'Page'
        
        code = f'''from playwright.sync_api import Page

class {class_name}:
    def __init__(self, page: Page):
        self.page = page
        self.url = "{self.dom['url']}"
    
    def navigate(self):
        self.page.goto(self.url)
        return self
'''
        
        # Generate methods for each element type
        for elem_type, elements in self.dom['elements'].items():
            if elements:
                for i, elem in enumerate(elements):
                    selector = elem.get('selector', '')
                    text = elem.get('text', '')[:30].replace('\n', ' ')
                    
                    if elem_type == 'buttons':
                        code += f'''
    def click_{elem_type}_{i}(self):
        """Click: {text}"""
        self.page.locator("{selector}").first.click()
        return self
'''
                    elif elem_type == 'links':
                        code += f'''
    def click_link_{i}(self):
        """Click link: {text}"""
        self.page.locator("{selector}").first.click()
        return self
'''
                    elif elem_type == 'inputs':
                        code += f'''
    def fill_input_{i}(self, value):
        """Fill: {text}"""
        self.page.locator("{selector}").first.fill(value)
        return self
'''
        
        return code
    
    def save_page_class(self, filename='page_objects.py'):
        """Save generated page object class"""
        code = self.generate_page_class()
        with open(filename, 'w') as f:
            f.write(code)
        return filename

if __name__ == '__main__':
    gen = PageObjectGenerator()
    file = gen.save_page_class()
    print(f"✓ Page object class generated: {file}")
