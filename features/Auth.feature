Feature: As a user i want to login

  Scenario: Login page
    Given I open browser
    When I click on Basic Auth
    And I input username and password i can login
    Then I go back on main page