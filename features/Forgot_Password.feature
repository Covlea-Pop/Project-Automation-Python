Feature: As a user i am able to reset my pwd
  Scenario: I can reset my pwd
     Given I open browser
    When I access Forgot Password page
    And I can reset my pwd
    Then I close window