import pytest
import cribbage_scorer


@pytest.mark.parametrize("starter, hand, expected_score, description", [
        ((5,"H"), [(7,"S"),(9,"S"), (2,"C"), (9,"H")], 2, "simple, double 9"),
        ((4,"H"), [(4,"S"),(9,"S"), (1,"C"), (9,"H")], 2, "simple, double 4"),
        ((11,"S"), [(12,"D"),(13,"S"), (1,"C"), (9,"H")], 3, "simple, 3 card run"),
        ((1,"S"), [(5,"D"),(10,"S"), (2,"C"), (6,"H")], 2, "simple, 15"),
        ((5,"H"), [(5,"S"),(4,"S"), (2,"S"), (6,"H")], 12, "mixed, 15s, double run"),
        ((5,"H"), [(6,"D"),(11,"H"), (4,"H"), (7,"C")], 9, "mixed, 15s, run, nob"),
        ((5,"H"), [(10,"S"),(8,"D"), (13,"C"), (8,"C")], 6, "mixed, 15s, pair")
    ])
def test_scores(starter, hand,   expected_score, description):

        calculated_score = cribbage_scorer.score(starter, hand)
        assert cribbage_scorer.score(starter, hand) == expected_score, \
            f"The calculated score was: {calculated_score}, the expected score: {expected_score}. " + \
            f"The starter card was: {starter} and hand was: {hand}" + \
            f"The hand description was: {description}"

