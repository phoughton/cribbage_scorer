import pytest
from cribbage_scorer import cribbage_scorer


@pytest.mark.parametrize("starter, hand, duplicates", [
        ((5, "H"), [(7, "S"), (9, "S"), (2, "C"), (5, "H")], ["5H"]),
        ((8, "H"), [(7, "S"), (9, "S"), (2, "H"), (8, "H")], ["8H"]),
        ((4, "H"), [(4, "H"), (5, "S"), (5, "S"), (9, "H")], ["4H", "5S"])
    ])
def test_duplicate_cards(starter, hand, duplicates):

    for duplicate in duplicates:
        with pytest.raises(ValueError, match=r".*Duplicate.*" + duplicate + ".*"):
            cribbage_scorer.show_calc_score(starter, hand)
