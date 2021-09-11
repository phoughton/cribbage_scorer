import pytest
from cribbage_scorer import cribbage_scorer


@pytest.mark.parametrize("hand, players, expected_count, expected_score, description", [
        ([(1, "S"), (2, "S")], ["Abi", "Bob"], 3, 0, "Simple ace and 2."),
        ([(4, "S")], ["Abi", "Bob"], 4, 0, "simple 1 card, 4"),
        ([(1, "H"), (10, "S")], ["Abi", "Bob"], 11, 0, "Simple ace and 10."),
        ([(5, "H"), (10, "S")], ["Abi", "Bob"], 15, 2, "fifteen for 2")
])
def test_simple_hands1(hand, players, expected_count, expected_score, description):

    calc_count, calc_score, calc_desc = cribbage_scorer.play_score_ongoing(hand)
    print(calc_count, calc_score, calc_desc)
    assert calc_score == expected_score, \
        f"The calculated score was: {calc_score}, the expected score: {expected_score}. " + \
        f"The calculated count was: {calc_count} and the expected : {expected_count} " + \
        f"The hand description was: {description} "


@pytest.mark.parametrize("hand, players, last_card, expected_count, expected_score, description", [
        ([(13, "S"), (12, "H"), (10, "S")], ["Abi", "Bob"], True, 30, 1, "Last card at 30"),
        ([(13, "S"), (12, "H"), (9, "S")], ["Abi", "Bob"], True, 30, 1, "Last card at 29"),
        ([(13, "S"), (12, "H"), (9, "S")], ["Abi", "Bob"], False, 30, 0, "Not last card at 29"),
        ([(13, "S"), (12, "H"), (10, "S"), (1, "D")], ["Abi", "Bob"], True, 31, 2, "Last card at 31")
])
def test_last_card(hand, players, last_card, expected_count, expected_score, description):

    calc_count, calc_score, calc_desc = cribbage_scorer.play_score_ongoing(hand, last_card)
    print(calc_count, calc_score, calc_desc)
    assert calc_score == expected_score, \
        f"The calculated score was: {calc_score}, the expected score: {expected_score}. " + \
        f"The calculated count was: {calc_count} and the expected : {expected_count}. " + \
        f"The hand description was: {description}"


@pytest.mark.parametrize("played_cards, players, expected_last_player", [
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
def test_last_player(played_cards, players, expected_last_player):

    calc_last_player = cribbage_scorer.last_player(played_cards, players)
    assert calc_last_player == expected_last_player, f"When played:{played_cards}, and players: {players}"


@pytest.mark.parametrize("hand, players, expected_count, expected_score, description", [
    ([(1, "S"), (2, "H"), (3, "S")], ["Abi", "Bob"], 6, 3, "Run of 3, in order"),
    ([(1, "S"), (3, "H"), (2, "S")], ["Abi", "Bob"], 6, 3, "Run of 3, out of order"),
    ([(5, "D"), (3, "S"), (1, "H"), (2, "S")], ["Abi", "Bob"], 11, 3, "Run of 3, out of order"),
    ([(4, "D"), (3, "S"), (1, "H"), (2, "S")], ["Abi", "Bob"], 10, 4, "Run of 4, out of order"),
    ([(5, "D"), (4, "D"), (2, "S"), (3, "H"), (2, "D")], ["Abi", "Bob"], 16, 0, "Double Run of 4, should not sore"),
    ([(1, "H"), (2, "S")], ["Abi", "Bob"], 3, 0, "run of 2"),
    ([(2, "S"), (3, "H"), (4, "S"), (5, "H"), (6, "S"), (7, "D")], ["Abi", "Bob"], 27, 6, "run of 6")
])
def test_runs(hand, players, expected_count, expected_score, description):

    calc_count, calc_score, calc_desc = cribbage_scorer.play_score_ongoing(hand)
    print(calc_count, calc_score, calc_desc)
    assert calc_score == expected_score, \
        f"The calculated score was: {calc_score}, the expected score: {expected_score}. " + \
        f"The calculated count was: {calc_count} and the expected : {expected_count} " + \
        f"The hand description was: {description} "


@pytest.mark.parametrize("hand, players, expected_count, expected_score, description", [
    ([(1, "S"), (3, "H"), (3, "S")], ["Abi", "Bob"], 7, 2, "Double"),
    ([(3, "S"), (3, "H"), (3, "D")], ["Abi", "Bob"], 9, 6, "Triple"),
    ([(3, "D"), (3, "H"), (3, "S"), (3, "C")], ["Abi", "Bob"], 12, 12, "Quadruple"),
    ([(1, "H"), (2, "S")], ["Abi", "Bob"], 3, 0, "Not a double"),
    ([(2, "S"), (3, "H"), (4, "S"), (4, "H"), (6, "S"), (7, "D")], ["Abi", "Bob"], 26, 0, "Historic double doesnt count")
])
def test_multiples(hand, players, expected_count, expected_score, description):

    calc_count, calc_score, calc_desc = cribbage_scorer.play_score_ongoing(hand)
    print(calc_count, calc_score, calc_desc)
    assert calc_score == expected_score, \
        f"The calculated score was: {calc_score}, the expected score: {expected_score}. " + \
        f"The calculated count was: {calc_count} and the expected : {expected_count} " + \
        f"The hand description was: {description} "
    assert calc_count == expected_count


@pytest.mark.parametrize("played_cards, players, expected_count, expected_scores, description", [
    ([(2, "S"), (3, "H"), (4, "S"), (4, "H"), (6, "S"), (7, "D")], ["Abi", "Bob"], 26, {"Abi": 3, "Bob": 3},
     "Low score to each"),
    ([(10, "S"), (3, "H"), (4, "S"), (4, "H"), (6, "S"), (4, "D")], ["Abi", "Bob"], 31, {"Abi": 0, "Bob": 4},
     "Bob, pair and 31"),
    ([(10, "S"), (3, "H"), (2, "S"), (4, "H"), (6, "S"), (4, "D")], ["Abi", "Bob"], 29, {"Abi": 2, "Bob": 4},
     "Abi: 15 for 2, Bob gets 1 for last card"),
    ([(10, "S"), (10, "H"), (10, "D"), (1, "H")], ["Abi", "Bob"], 31, {"Abi": 6, "Bob": 4},
     "Abi 3 of a kind, Bob pair and 31"),
    ([(10, "S"), (10, "H"), (10, "D"), (1, "H")], ["Abi", "Bob", "Charles"], 31, {"Abi": 2, "Bob": 2, "Charles": 6},
     "Charles 3 of a kind, Bob pair and Abi gets 31")
])
def test_whole_play_scoring(played_cards, players, expected_count, expected_scores, description):

    calc_scores, calc_count, play_log = cribbage_scorer.play_calc_score_set(played_cards, players)
    print(calc_scores, calc_count, play_log)
    assert calc_scores == expected_scores, \
        f"The calculated score was: {calc_scores}, the expected score: {expected_scores}. " + \
        f"The calculated count was: {calc_count} and the expected : {expected_count} " + \
        f"The play log was: {play_log} "
    assert calc_count == expected_count


@pytest.mark.parametrize("played_cards, players, expected_count, expected_scores, description", [
    ([(1, "S"), (3, "H"), (4, "S"), (4, "H"), (7, "S"), (6, "D"), (0, "GO"), (6, "C")], ["Abi", "Bob"], 31, {"Abi": 0, "Bob": 6},
     "Abi GOs and Bob gets 2nd pair"),
    ([(1, "S"), (3, "H"), (4, "S"), (4, "H"), (7, "S"), (6, "D"), (0, "GO"), (6, "C")], ["Abi", "Bob", "Charles"], 31,
     {"Abi": 2, "Bob": 4, "Charles": 0},
     "Abi gets pair, Bob gets 2nd pair and 31, Charles gets nothing"),
    ([(1, "S"), (3, "H"), (4, "S"), (4, "H"), (7, "S"), (6, "D"), (0, "GO"), (0, "GO"), (6, "C")],
     ["Abi", "Bob", "Charles"], 31,
     {"Abi": 2, "Bob": 0, "Charles": 4},
     "Abi gets pair, Bob gets 0, and Charles gets 2nd pair and 31"),
    ([(1, "S"), (3, "H"), (4, "S"), (4, "H"), (7, "S"), (6, "D"), (0, "GO"), (0, "GO"), (6, "C")],
     ["Abi", "Bob", "Charles", "David"], 31,
     {"Abi": 4, "Bob": 0, "Charles": 0, "David": 2},
     "David gets pair, Bob & Charles get 0, and Abi gets 2nd pair and 31")
])
def test_whole_play_scoring_with_go(played_cards, players, expected_count, expected_scores, description):

    calc_scores, calc_count, play_log = cribbage_scorer.play_calc_score_set(played_cards, players)
    print(calc_scores, calc_count, play_log)
    assert calc_scores == expected_scores, \
        f"The calculated score was: {calc_scores}, the expected score: {expected_scores}. " + \
        f"The calculated count was: {calc_count} and the expected : {expected_count} " + \
        f"The play log was: {play_log} "
    assert calc_count == expected_count


@pytest.mark.parametrize("cut_card, players, dealer, expected_scores, description", [
    ((11, "S"), ["Abi", "Bob"], "Bob", {"Abi": 0, "Bob": 2}, "Bob dealer when cut gets Jack"),
    ((11, "S"), ["Abi", "Bob"], "Abi", {"Abi": 2, "Bob": 0}, "Abi dealer when cut gets Jack"),
    ((1, "D"), ["Abi", "Bob"], "Bob", {"Abi": 0, "Bob": 0}, "No-one cuts Jack"),
    ((10, "H"), ["Abi", "Bob"], "Abi", {"Abi": 0, "Bob": 0}, "No-one cuts Jack")
])
def test_cut_score(cut_card, players, dealer, expected_scores, description):

    calc_scores, msg = cribbage_scorer.cut_calc_score(cut_card, players, dealer)
    print(calc_scores, msg)
    assert calc_scores == expected_scores, \
        f"The calculated score was: {calc_scores}, the expected score: {expected_scores}. "
