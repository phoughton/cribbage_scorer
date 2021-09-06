import pytest
from cribbage_scorer import cribbage_scorer


@pytest.mark.parametrize("played_cards, duplicates", [
        ( [(7, "S"), (9, "S"), (2, "C"), (7, "S")], ["7S"]),
        ( [(7, "S"), (8, "H"), (2, "H"), (8, "H")], ["8H"]),
        ( [(5, "H"), (5, "H"), (5, "S"), (5, "S"), (0, "GO"), (0, "GO")], ["5H", "5S"])
    ])
def test_duplicate_cards_play_set(played_cards, duplicates):

    for duplicate in duplicates:
        with pytest.raises(ValueError, match=r".*Duplicate.*" + duplicate + ".*"):
            cribbage_scorer.play_calc_score_set(played_cards, ["Jack", "Jill"])



@pytest.mark.parametrize("played_cards, duplicates", [
        ( [(7, "S"), (9, "S"), (2, "C"), (7, "S")], ["7S"]),
        ( [(7, "S"), (8, "H"), (2, "H"), (8, "H")], ["8H"]),
        ( [(5, "H"), (5, "H"), (5, "S"), (5, "S"), (0, "GO"), (0, "GO")], ["5H", "5S"])
    ])
def test_duplicate_cards_play_ongoing(played_cards, duplicates):

    for duplicate in duplicates:
        with pytest.raises(ValueError, match=r".*Duplicate.*" + duplicate + ".*"):
            cribbage_scorer.play_score_ongoing(played_cards, ["Jack", "Jill"])


