from collections import defaultdict
import itertools


def score(starter, hand):
    running_score = 0
    running_msg = ""

    multiples_score, multiples_msg = multiples(starter, hand)
    running_score += multiples_score
    running_msg = running_msg + multiples_msg

    fifteens_score, fifteens_msg = fifteens(starter, hand)
    running_score += fifteens_score
    running_msg = running_msg + fifteens_msg

    return running_score, running_msg


def fifteens(starter, hand):
    all_cards = hand + [starter]
    print("Combined hand: " + str(all_cards))

    running_score = 0
    score_msg = ""

    combinations_2_cards = itertools.combinations(all_cards, 2)
    for two_card_sequence in combinations_2_cards:
        if two_card_sequence[0][0] + two_card_sequence[1][0] == 15:
            running_score += 2
            score_msg = score_msg + f"15 from {two_card_sequence}"

    combinations_3_cards = itertools.combinations(all_cards, 3)
    for three_card_sequence in combinations_3_cards:
        if three_card_sequence[0][0] + three_card_sequence[1][0] + three_card_sequence[2][0] == 15:
            running_score += 2
            score_msg = score_msg + f"15 from {three_card_sequence}"

    return running_score, score_msg


def multiples(starter, hand):
    all_cards = hand + [starter]
    print("Combined hand: " + str(all_cards))

    multiples_counter = defaultdict(lambda: 0)
    for card in all_cards:
        multiples_counter[card[0]] += 1

    multiples_found = {}
    for card_name, count in multiples_counter.items():
        if count > 1:
            multiples_found[card_name] = count

    score_total = 0
    score_msg = ""
    for card, count in multiples_found.items():
        if count == 2:
            score_total += 2
            score_msg = score_msg + f"2 points for double {card}s, "
        elif count == 3:
            score_total += 6
            score_msg = score_msg + f"6 points for triple {card}s, "
        elif count == 4:
            score_total += 12
            score_msg = score_msg + f"12 points for quadruple {card}s, "
        else:
            raise Exception(f"An illegal multiple  of {count} was found in hand: {hand}")

    return score_total, score_msg
