from behave import given, when, then
import requests

@given('the API base URL is "{url}"')
def set_base_url(context, url):
    context.base_url = url

@when('I send a GET request to "{endpoint}"')
def send_get_request(context, endpoint):
    context.response = requests.get(f"{context.base_url}{endpoint}")

@when('I send a POST request to "{endpoint}" with body')
def send_post_request(context, endpoint):
    context.response = requests.post(f"{context.base_url}{endpoint}", json=context.text)

@then('the response status code should be {status_code:d}')
def check_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"

@then('the response should contain products data')
def check_products_data(context):
    data = context.response.json()
    assert 'data' in data or isinstance(data, list), "Response should contain products data"
    if 'data' in data:
        assert len(data['data']) > 0, "Products data should not be empty"

@then('the response should have product details')
def check_product_details(context):
    data = context.response.json()
    assert 'id' in data, "Product should have an ID"
    assert 'name' in data, "Product should have a name"

@then('the response should be a list')
def check_is_list(context):
    data = context.response.json()
    assert isinstance(data, list), "Response should be a list"
