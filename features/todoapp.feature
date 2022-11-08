Feature: Testing web applications
  @web
  Scenario: Mark all todos done and check remaining 0
    Given I am on the todo page
    When I click done on all todos
    Then Remaining todos should read 0