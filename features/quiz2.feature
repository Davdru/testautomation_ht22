Feature: Test av quiz-programmet med ny teststruktur
  @quiz
  Scenario: Flera frågor i samma scenario
    Given A quiz program
    And a question "Vad är meningen med livet, universum och allting?"
      | answer  | correct |
      | 99      | False   |
      | 42      | True    |
      | 12      | False   |
      | Ingen aning | False |
    And The user answers 2
    And a question "Vilken funktion använder vi för att skriva ut text i terminalen?"
      | answer  | correct |
      | input()      | False   |
      | assert      | False   |
      | print()      | True   |
      | Ingen aning | False |
    And The user answers 3
    When The program is run
    Then The result should be You answered 2 of 2 correct!

# Implementera steps så att testet fungerar