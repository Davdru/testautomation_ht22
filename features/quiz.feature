Feature: Behave tests of quiz game
  @quiz
  Scenario: Quiz increases correct count on correct answer
    Given A quiz program
    And There is one question
    And Answer 1 is correct
    When The user answers 1
    And  The program is run
    Then The result should be You answered 1 of 1 correct!

  @quiz
  Scenario: Fråga i scenario, svara rätt
    Given A quiz program
    And a question "Vad är meningen med livet, universum och allting?"
      | answer  | correct |
      | 99      | False   |
      | 42      | True    |
      | 12      | False   |
      | Ingen aning | False |
    When The user answers 2
    And The program is run
    Then The result should be You answered 1 of 1 correct!

  @quiz
  Scenario: Fråga i scenario, svara fel
    Given A quiz program
    And a question "Vad är meningen med livet, universum och allting?"
      | answer  | correct |
      | 99      | False   |
      | 42      | True    |
      | 12      | False   |
      | Ingen aning | False |
    When The user answers 3
    And The program is run
    Then The result should be You answered 0 of 1 correct!

# Uppgift.
  # Skapa scenario med flera frågor, du skall kunna ange vilka svar som skall ges
  # Du behöver ändra koden för TestUser och stegimplementationerna för styra vad användaren svarar