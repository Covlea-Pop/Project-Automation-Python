Feature: As a user i want to able to login
  Scenario: Use Form Authentication
    Given I open browser
    When I access Login  page
    And I can login with valid username and pwd
    Then I close window