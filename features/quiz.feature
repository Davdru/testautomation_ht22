Feature: Behave tests of quiz game
  @quiz
  Scenario: Quiz increases correct count on correct answer
    Given A quiz program
    And There is one question
    And Answer 1 is correct
    When The user answers 1
    And  The program is run
    Then The result should be 1 of 1 questions correct