Feature: Validate registered user purchase flow

  Background:
    Given the application context is loaded
    And business rules are defined

  Scenario: Validate registered user purchase flow
    Given I am a "Registered User"
    And I am logged in with valid credentials
    When I browse products
    And I add a product to cart
    And I proceed to checkout
    Then the order total should respect business rules
    And I should see payment options
