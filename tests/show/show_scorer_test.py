import pytest
from cribbage_scorer import cribbage_scorer


@pytest.mark.parametrize("starter, hand, expected_score, description", [
        ((5, "H"), [(7, "S"), (9, "S"), (2, "C"), (9, "H")], 2, "simple, double 9"),
        ((5, "H"), [(7, "S"), (9, "S"), (2, "H"), (9, "H")], 2, "simple, double 9. 2 pairs of suits"),
        ((4, "H"), [(4, "S"), (9, "S"), (1, "C"), (9, "H")], 4, "simple, double 4 and double 9"),
        ((4, "H"), [(4, "S"), (9, "S"), (1, "C"), (4, "D")], 6, "simple, triple 4 "),
        ((4, "H"), [(4, "S"), (9, "S"), (4, "C"), (4, "D")], 12, "simple, quadruple 4 ")
    ])
def test_multiples(starter, hand, expected_score, description):

    calculated_score = cribbage_scorer.show_calc_score(starter, hand)
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

    calculated_score = cribbage_scorer.show_calc_score(starter, hand)
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

    calculated_score = cribbage_scorer.show_calc_score(starter, hand)
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
    calculated_score = cribbage_scorer.show_calc_score(starter, hand)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}, " + \
        f"The hand description was: {description} "


@pytest.mark.parametrize("starter, hand, expected_score, description", [
    ((11, "C"), [(5, "H"), (5, "C"), (10, "H"), (12, "C")], 17, "?"),
    ((1, "C"), [(1, "H"), (2, "C"), (3, "H"), (3, "C")], 16, "?")

])
def test_multi_and_run_but_not_multirun(starter, hand, expected_score, description):
    calculated_score = cribbage_scorer.show_calc_score(starter, hand)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}, " + \
        f"The hand description was: {description} "


@pytest.mark.parametrize("starter, hand, crib, expected_score, description", [
    ((8, "S"), [(12, "S"), (13, "S"), (1, "S"), (2, "S")], False, 5, "5 card flush"),
    ((8, "S"), [(12, "S"), (13, "S"), (1, "S"), (2, "S")], True, 5,  "5 card flush (crib)"),
    ((8, "D"), [(12, "S"), (13, "S"), (1, "S"), (2, "S")], True, 0, "Not a flush, as it is a crib"),
    ((8, "D"), [(12, "S"), (13, "S"), (1, "S"), (2, "S")], False, 4, "4 card flush"),
    ((8, "S"), [(12, "S"), (13, "S"), (1, "S"), (2, "H")], False, 0, "Not a flush."),
    ((8, "S"), [(12, "D"), (13, "S"), (1, "C"), (2, "H")], False, 0, "Not a flush."),
    ((6, 'C'), [(7, 'C'), (7, 'H'), (8, 'H'), (5, 'C')], False, 14, "Not a flush")
])
def test_flushes(starter, hand, crib, expected_score, description):
    calculated_score = cribbage_scorer.show_calc_score(starter, hand, crib)
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
    calculated_score = cribbage_scorer.show_calc_score(starter, hand, crib)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}, " + \
        f"The hand description was: {description} "
    assert calculated_score[1] == description


@pytest.mark.parametrize("starter, hand, expected_score, description", [
    ((5, "D"), [(5, "H"), (5, "S"), (5, "C"), (11, "D")], 29, "Perfect hand, 29"),
    ((10, "H"), [(5, "D"), (5, "S"), (5, "C"), (5, "H")], 28, "2nd best hand, 28"),
    ((9, "D"), [(3, "D"), (3, "S"), (3, "C"), (3, "H")], 24, "1. 3rd best hand, 24"),
    ((6, "H"), [(6, "S"), (5, "D"), (5, "C"), (4, "H")], 24, "2. 3rd best hand, 24"),
    ((5, "H"), [(11, "H"), (11, "D"), (5, "C"), (5, "S")], 23, "4th best hand, 23"),
    ((10, "S"), [(10, "C"), (5, "D"), (5, "C"), (5, "H")], 22, "5th best hand, 22"),
    ((9, "S"), [(2, "C"), (2, "D"), (2, "H"), (2, "S")], 20, "1. 6th best hand, 20"),
    ((1, "C"), [(5, "C"), (5, "D"), (5, "H"), (5, "S")], 20, "2. 6th best hand, 20"),
    ((6, "C"), [(9, "C"), (9, "D"), (9, "H"), (9, "S")], 20, "3. 6th best hand, 20"),
    ((13, "C"), [(12, "S"), (5, "D"), (5, "H"), (5, "S")], 20, "4. 6th best hand, 20"),
    ((5, "D"), [(4, "H"), (4, "S"), (3, "H"), (3, "C")], 20, "5. 6th best hand, 20"),
    ((10, "S"), [(1, "D"), (1, "H"), (1, "S"), (1, "C")], 12, "1. 12, from aces"),
    ((5, "S"), [(1, "D"), (1, "H"), (1, "S"), (1, "C")], 12, "2. 12, from aces"),
    ((13, "H"), [(5, "H"), (10, "H"), (11, "H"), (12, "H")], 18, "18, highest with 5pt flush")
])
def test_etc_hands__crib_neutral(starter, hand, expected_score, description):
    for crib in [False, True]:
        calculated_score = cribbage_scorer.show_calc_score(starter, hand, crib)
        print(calculated_score[1])
        assert calculated_score[0] == expected_score, \
            f"The calc score was: {calculated_score}, the expected score: {expected_score}. " + \
            f"The starter card was: {starter} and hand was: {hand}, " + \
            f"The hand description was: {description}. " + \
            f"Crib card status: {crib}"


@pytest.mark.parametrize("starter, hand, crib, expected_score, description", [
    ((6, "D"), [(6, "S"), (5, "S"), (4, "S"), (3, "S")], False, 20, "6. 6th best hand"),
    ((7, "S"), [(8, "D"), (7, "D"), (6, "D"), (1, "D")], False, 20, "7. 6th best hand"),
    ((6, "D"), [(6, "S"), (5, "S"), (4, "S"), (3, "S")], True, 16, "6. 6th best hand, but crib"),
    ((7, "S"), [(8, "D"), (7, "D"), (6, "D"), (1, "D")], True, 16, "7. 6th best hand, but crib"),
])
def test_etc_hands__crib_affected(starter, hand, crib, expected_score, description):
    calculated_score = cribbage_scorer.show_calc_score(starter, hand, crib)
    print(calculated_score[1])
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}, " + \
        f"The hand description was: {description} "

