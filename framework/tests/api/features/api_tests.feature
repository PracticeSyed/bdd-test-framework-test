Feature: API Testing - Practice Software Testing
  
  Scenario: Get all products
    Given the API base URL is "https://api.practicesoftwaretesting.com"
    When I send a GET request to "/products"
    Then the response status code should be 200
    And the response should contain products data
  
  Scenario: Get single product by ID
    Given the API base URL is "https://api.practicesoftwaretesting.com"
    When I send a GET request to "/products/01KVQCC6BV4YKZZ76PX3GXT71M"
    Then the response status code should be 200
    And the response should have product details
  
  Scenario: Get all categories
    Given the API base URL is "https://api.practicesoftwaretesting.com"
    When I send a GET request to "/categories"
    Then the response status code should be 200
    And the response should be a list
  
  Scenario: Get all brands
    Given the API base URL is "https://api.practicesoftwaretesting.com"
    When I send a GET request to "/brands"
    Then the response status code should be 200
    And the response should be a list
  
  Scenario: Search products by name
    Given the API base URL is "https://api.practicesoftwaretesting.com"
    When I send a GET request to "/products?q=hammer"
    Then the response status code should be 200
    And the response should contain products data
  
  Scenario: Filter products by category
    Given the API base URL is "https://api.practicesoftwaretesting.com"
    When I send a GET request to "/products?by_category=01KVQ5GFQ4S61JH2SSYKD60ET8"
    Then the response status code should be 200
  
  Scenario: Get products with pagination
    Given the API base URL is "https://api.practicesoftwaretesting.com"
    When I send a GET request to "/products?page=1"
    Then the response status code should be 200
    And the response should contain products data
  
  Scenario: Invalid product ID returns 404
    Given the API base URL is "https://api.practicesoftwaretesting.com"
    When I send a GET request to "/products/invalid-id-12345"
    Then the response status code should be 404
