Feature: Practice Software Testing Site
  AI-powered automated testing with auto-updating page objects

  Scenario: Navigate to practice site
    Given I open the practice software testing site
    Then the page should be loaded

  Scenario: Verify page title
    Given I open the practice software testing site
    Then the page title should contain "moment"

  Scenario: Check footer links
    Given I open the practice software testing site
    Then I should see "Cloudflare" link
    And I should see "Privacy" link

  Scenario: Verify page elements
    Given I open the practice software testing site
    Then the page should have a footer
    And the page should have main content
