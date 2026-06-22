from behave import given, when, then
from playwright.sync_api import sync_playwright
import importlib.util
import sys

def load_page_object():
    """Dynamically load generated page object"""
    spec = importlib.util.spec_from_file_location("page_objects", "tests/bdd/pages/page_objects.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["page_objects"] = module
    spec.loader.exec_module(module)
    return module

@given('I open the practice software testing site')
def open_site(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)
    context.page = context.browser.new_page()
    
    # Load auto-generated page object
    page_module = load_page_object()
    PageClass = getattr(page_module, list(vars(page_module).keys())[-1])
    context.page_object = PageClass(context.page)
    context.page_object.navigate()

@when('I interact with element "{element_method}"')
def interact_element(context, element_method):
    method = getattr(context.page_object, element_method)
    method()

@when('I fill "{element_method}" with "{value}"')
def fill_element(context, element_method, value):
    method = getattr(context.page_object, element_method)
    method(value)

@then('the page should be loaded')
def verify_loaded(context):
    assert context.page.title(), "Page not loaded"
    print(f"✓ Page loaded: {context.page.title()}")

@then('the page title should contain "{text}"')
def verify_title_contains(context, text):
    title = context.page.title()
    assert text.lower() in title.lower(), f"Title '{title}' does not contain '{text}'"
    print(f"✓ Title contains: {text}")

@then('I should see "{link_text}" link')
def verify_link(context, link_text):
    link = context.page.locator(f"text={link_text}")
    assert link.count() > 0, f"Link '{link_text}' not found"
    print(f"✓ Found link: {link_text}")

@then('the page should have a footer')
def verify_footer(context):
    footer = context.page.locator("div.footer, footer, [role='contentinfo']")
    assert footer.count() > 0, "Footer not found"
    print("✓ Footer exists")

@then('the page should have main content')
def verify_main(context):
    main = context.page.locator("div.main-wrapper, main, [role='main']")
    assert main.count() > 0, "Main content not found"
    print("✓ Main content exists")
