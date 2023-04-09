Feature: Cribbage Scorer

  Scenario: Verify scores after cutting
    Given the cut card is "<cut_card>"
#    When the players are <players> and the dealer is <dealer>
#    Then the scores should be <expected_scores>

    Examples:
      | cut_card      | players     | dealer | expected_scores            | description                          |
      | Jack of Spades | Abi, Bob    | Bob    | {"Abi": 0, "Bob": 2}       | Bob dealer when cut gets Jack       |
      | Jack of Spades | Abi, Bob    | Abi    | {"Abi": 2, "Bob": 0}       | Abi dealer when cut gets Jack       |
      | Ace of Diamonds | Abi, Bob   | Bob    | {"Abi": 0, "Bob": 0}       | No-one cuts Jack                    |
      | Ten of Hearts  | Abi, Bob    | Abi    | {"Abi": 0, "Bob": 0}       | No-one cuts Jack                    |
