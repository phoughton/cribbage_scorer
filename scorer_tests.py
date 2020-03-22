import pytest
import cribbage_scorer


@pytest.mark.parametrize("starter, hand, expected_score, description", [
        ((5, "H"), [(7, "S"), (9, "S"), (2, "C"), (9, "H")], 2, "simple, double 9"),
        ((4, "H"), [(4, "S"), (9, "S"), (1, "C"), (9, "H")], 4, "simple, double 4 and double 9"),
        ((4, "H"), [(4, "S"), (9, "S"), (1, "C"), (4, "D")], 6, "simple, triple 4 "),
        ((4, "H"), [(4, "S"), (9, "S"), (4, "C"), (4, "D")], 12, "simple, quadruple 4 ")
    ])
def test_multiples(starter, hand, expected_score, description):

    calculated_score = cribbage_scorer.calc_score(starter, hand)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}" + \
        f"The hand description was: {description}"


@pytest.mark.parametrize("starter, hand, expected_score, description", [
        ((1, "S"), [(5, "D"), (10, "S"), (2, "C"), (6, "H")], 2, "simple, 15,= from 1 x 2 cards"),
        ((2, "S"), [(5, "D"), (10, "S"), (9, "C"), (6, "H")], 4, "simple, 2 x 15 from 2 x 2 cards"),
        ((2, "S"), [(3, "D"), (10, "S"), (7, "C"), (9, "H")], 2, "simple, 1 x 15 from 1 x 3 cards"),
        ((1, "S"), [(2, "D"), (4, "S"), (5, "C"), (7, "H")], 2, "simple, 1 x 15 from 1 x 4 cards"),
        ((1, "S"), [(2, "D"), (4, "S"), (6, "C"), (6, "H")], 4, "Pair and 1 x 15 from 1 x 5 cards")
])
def test_fifteens(starter, hand, expected_score, description):

    calculated_score = cribbage_scorer.calc_score(starter, hand)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}" + \
        f"The hand description was: {description}"


@pytest.mark.parametrize("starter, hand, expected_score, description", [
        ((8, "S"), [(12, "D"), (13, "S"), (1, "C"), (2, "H")], 0, ""),
        ((11, "S"), [(12, "D"), (13, "S"), (1, "C"), (2, "H")], 3, "Run of 3 cards (3pts)"),
        ((10, "S"), [(11, "D"), (12, "S"), (13, "C"), (1, "H")], 4, "Run of 4 cards (4pts)"),
        ((9, "D"), [(10, "D"), (11, "S"), (12, "C"), (13, "H")], 5, "Run of 5 cards (5pts)")
])
def test_runs(starter, hand, expected_score, description):

    calculated_score = cribbage_scorer.calc_score(starter, hand)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}, " + \
        f"The hand description was: {description} "
    assert calculated_score[1] == description


@pytest.mark.parametrize("starter, hand, expected_score, description", [
    ((1, "S"), [(2, "D"), (2, "S"), (3, "C"), (6, "H")], 8, "double run of 3"),
    ((1, "S"), [(2, "D"), (2, "S"), (2, "C"), (3, "H")], 15, "triple, run of 3"),
    ((1, "S"), [(1, "D"), (2, "S"), (2, "C"), (3, "H")], 16, "double double run of 3"),
    ((1, "S"), [(2, "D"), (2, "S"), (3, "C"), (4, "H")], 10, "double run of 4")
])
def test_multi_runs(starter, hand, expected_score, description):
    calculated_score = cribbage_scorer.calc_score(starter, hand)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}, " + \
        f"The hand description was: {description} "


@pytest.mark.parametrize("starter, hand, crib, expected_score, description", [
    ((8, "S"), [(12, "S"), (13, "S"), (1, "S"), (2, "S")], False, 5, "5 card flush"),
    ((8, "S"), [(12, "S"), (13, "S"), (1, "S"), (2, "S")], True, 4,  "4 card flush (not 5 as crib)"),
    ((8, "D"), [(12, "S"), (13, "S"), (1, "S"), (2, "S")], False, 4, "4 card flush"),
    ((8, "S"), [(12, "S"), (13, "S"), (1, "S"), (2, "H")], False, 0, "Not a flush."),
    ((8, "S"), [(12, "D"), (13, "S"), (1, "C"), (2, "H")], False, 0, "Not a flush.")
])
def test_flushes(starter, hand, crib, expected_score, description):
    calculated_score = cribbage_scorer.calc_score(starter, hand, crib)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}, " + \
        f"The hand description was: {description} "


@pytest.mark.parametrize("starter, hand, crib, expected_score, description", [
    ((8, "D"), [(10, "D"), (13, "S"), (1, "C"), (11, "H")], False, 0, ""),
    ((8, "H"), [(10, "D"), (13, "S"), (1, "C"), (11, "H")], False, 1, "One for his nobs (1pt)")
])
def test_his_nobs(starter, hand, crib, expected_score, description):
    calculated_score = cribbage_scorer.calc_score(starter, hand, crib)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}, " + \
        f"The hand description was: {description} "
    assert calculated_score[1] == description


@pytest.mark.parametrize("starter, hand, crib, expected_score, description", [
    ((5, "D"), [(5, "D"), (5, "S"), (5, "C"), (11, "D")], False, 29, "Perfect hand")
])
def test_etc_hands(starter, hand, crib, expected_score, description):
    calculated_score = cribbage_scorer.calc_score(starter, hand, crib)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}, " + \
        f"The hand description was: {description} "
