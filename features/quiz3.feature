Feature: Ny struktur för att ange frågor i quizet
  @quiz
  Scenario: Svara fel på en fråga skall ge 0 av 1 rätt
    Given A quiz program
    And question with
      | prompt                                          | times_asked | times_correct | answer | correct |
      | Vad är meningen med livet universum och allting | 2           | 1             |        |         |
      |                                                 |             |               | 42     | True    |
      |                                                 |             |               | 12     | False   |
      |                                                 |             |               | 99     | False   |
    When The user answers 2
    And The program is run
    Then The result should be You answered 0 of 1 correct!

    @quiz
    Scenario: 5. Två frågor, svara rätt på en
      Given A quiz program
      And question with
        | prompt                                          | times_asked | times_correct | answer | correct |
        | Vad är meningen med livet universum och allting | 2           | 1             |        |         |
        |                                                 |             |               | 42     | True    |
        |                                                 |             |               | 12     | False   |
        |                                                 |             |               | 99     | False   |
      And question with
        | prompt                                                           | times_asked | times_correct | answer     | correct |
        | Vilken funktion använder vi för att skriva ut saker i terminalen | 10          | 9             |            |         |
        |                                                                  |             |               | print()    | True    |
        |                                                                  |             |               | input(">") | False   |
        |                                                                  |             |               | len        | False   |
      When The user answers 2,1
      And The program is run
      Then The result should be You answered 1 of 2 correct!

      # Få testerna att fungera, ny kod behövs för att tolka och skapa frågor i step-filen