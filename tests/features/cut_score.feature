Feature: Cut score calculation
  As a player of cribbage
  I want the cut score to be calculated correctly
  So that the game can proceed fairly

  Scenario Outline: Calculate cut score based on cut card, players and dealer
    Given a cut card <cut_card>
    And the players are <players>
    And the dealer was <dealer>
    When the cut score is calculated
    Then Abi scores <expected_score_abi> and Bob scores <expected_score_bob>

    Examples:
      | cut_card  | players        | dealer | expected_score_abi | expected_score_bob | description                       |
      | (11, "S") | ["Abi", "Bob"] | Bob    |  0                 | 2                  | Bob dealer when cut gets Jack     |
      | (11, "S") | ["Abi", "Bob"] | Abi    |  2                 | 0                  | Abi dealer when cut gets Jack     |
      | (1, "D")  | ["Abi", "Bob"] | Bob    |  0                 | 0                  | No-one cuts Jack                  |
      | (10, "H") | ["Abi", "Bob"] | Abi    |  0                 | 0                  | No-one cuts Jack                  |
