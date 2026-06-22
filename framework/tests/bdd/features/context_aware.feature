Feature: Context-Aware E-commerce Testing
  As a test engineer
  I want to validate critical user flows
  Based on business rules and user personas

  Background:
    Given the application context is loaded
    And business rules are defined

  @critical @guest_user
  Scenario: Guest user browses products
    Given I am a "Guest User"
    When I navigate to the product catalog
    Then I should see available products
    And I should be able to view product details
    But I should not see checkout options

  @critical @registered_user
  Scenario: Registered user completes purchase flow
    Given I am a "Registered User"
    And I am logged in with valid credentials
    When I browse products
    And I add a product to cart
    And I proceed to checkout
    Then the order total should respect business rules
    And I should see payment options

  @business_rule
  Scenario: Validate minimum order value
    Given I am a "Registered User"
    And I have items in cart totaling "$8"
    When I attempt to checkout
    Then I should see "Minimum order value: $10" message

  @business_rule
  Scenario: Validate free shipping threshold
    Given I am a "Registered User"
    And I have items in cart totaling "$55"
    When I view cart summary
    Then shipping cost should be "$0"
