import pytest
import cribbage_scorer


@pytest.mark.parametrize("starter, hand, expected_score, description", [
        ((5, "H"), [(7, "S"), (9, "S"), (2, "C"), (9, "H")], 2, "simple, double 9"),
        ((4, "H"), [(4, "S"), (9, "S"), (1, "C"), (9, "H")], 4, "simple, double 4 and double 9"),
        ((4, "H"), [(4, "S"), (9, "S"), (1, "C"), (4, "D")], 6, "simple, triple 4 "),
        ((4, "H"), [(4, "S"), (9, "S"), (4, "C"), (4, "D")], 12, "simple, quadruple 4 ")
    ])
def test_multiples(starter, hand, expected_score, description):

    calculated_score = cribbage_scorer.score(starter, hand)
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}" + \
        f"The hand description was: {description}"


@pytest.mark.parametrize("starter, hand, expected_score, description", [
        ((1, "S"), [(5, "D"), (10, "S"), (2, "C"), (6, "H")], 2, "simple, 15,= from 1 x 2 cards"),
        ((2, "S"), [(5, "D"), (10, "S"), (9, "C"), (6, "H")], 4, "simple, 2 x 15 from 2 x 2 cards"),
        ((2, "S"), [(3, "D"), (10, "S"), (7, "C"), (9, "H")], 2, "simple, 1 x 15 from 1 x 3 cards"),
        ((2, "S"), [(3, "D"), (5, "S"), (6, "C"), (8, "H")], 2, "simple, 1 x 15 from 1 x 3 cards")
])
def test_fifteens(starter, hand, expected_score, description):

    calculated_score = cribbage_scorer.score(starter, hand)
    assert calculated_score[0] == expected_score, \
        f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
        f"The starter card was: {starter} and hand was: {hand}" + \
        f"The hand description was: {description}"

# ((11,"S"), [(12,"D"),(13,"S"), (1,"C"), (9,"H")], 3, "simple, 3 card run"),
# ((5,"H"), [(5,"S"),(4,"S"), (2,"S"), (6,"H")], 12, "mixed, 15s, double run"),
# ((5,"H"), [(6,"D"),(11,"H"), (4,"H"), (7,"C")], 9, "mixed, 15s, run, nob"),
# ((5,"H"), [(10,"S"),(8,"D"), (13,"C"), (8,"C")], 6, "mixed, 15s, pair")
