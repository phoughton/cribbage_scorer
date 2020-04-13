import pytest
import cribbage_scorer
import random


@pytest.fixture(params=range(0, 1000))
def card_sets(request):
        suits = ['H', 'C', 'S', 'D']
        ranks = range(1, 13)
        cards = set()
        while len(cards) < 5:
            suit = random.choice(suits)
            rank = random.choice(ranks)
            cards.add((rank, suit))
        return list(cards)


def test_for_impossible_scores(card_sets):

    starter_card = card_sets.pop()
    hand = card_sets

    calculated_score = cribbage_scorer.show_calc_score(starter_card, hand)

    assert calculated_score[0] not in [19, 25, 26, 27], \
        f"The calculated score was: {calculated_score}, this was an impossible score " + \
        f"The starter card was: {starter_card} and hand was: {hand}, "

