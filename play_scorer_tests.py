import pytest
import cribbage_scorer


@pytest.mark.parametrize("hand, players, expected_count, expected_score, description", [
        ([(1, "S"), (2, "S")], ["Abi", "Bob"], 3, 0, "Simple ace and 2."),
        ([(4, "S")], ["Abi", "Bob"], 4, 0, "simple 1 card, 4"),
        ([(1, "H"), (10, "S")], ["Abi", "Bob"], 11, 0, "Simple ace and 10."),
        ([(5, "H"), (10, "S")], ["Abi", "Bob"], 15, 2, "fifteen for 2")
])
def test_simple_hands1(hand, players, expected_count, expected_score, description):

    calc_count, calc_score, calc_desc = cribbage_scorer.play_calc_score(hand, [])
    print(calc_count, calc_score, calc_desc)
    assert calc_score == expected_score, \
        f"The calculated score was: {calc_score}, the expected score: {expected_score}. " + \
        f"The calculated count was: {calc_count} and the expected : {expected_count}" + \
        f"The hand description was: {description}"


@pytest.mark.parametrize("played_cards, players, last_player", [
        ([], ["Abi", "Bob"], None),
        ([(1, "S"), (2, "S")], ["Abi", "Bob"], "Bob"),
        ([(4, "S")], ["Abi", "Bob"], "Abi"),
        ([(1, "H"), (10, "S")], ["Abi", "Bob"], "Bob"),
        ([(1, "H"), (10, "S"), (10, "D")], ["Abi", "Bob"], "Abi"),
        ([(5, "H"), (10, "S"), (5, "H")], ["Abi", "Bob"], "Abi"),
        ([(1, "H"), (10, "S")], ["Abi", "Bob", "Charles"], "Bob"),
        ([(5, "H"), (10, "S"), (5, "H")], ["Abi", "Bob", "Charles", "David"], "Charles"),
        ([(5, "H"), (5, "S"), (5, "H"), (5, "C"), (1, "S"), (1, "H")], ["Abi", "Bob", "Charles", "David"], "Bob")

])
def test_last_player(played_cards, players, last_player):

    calc_last_player = cribbage_scorer.last_player(played_cards, players)
    assert calc_last_player == last_player, f"When played:{played_cards}, and players: {players}"
