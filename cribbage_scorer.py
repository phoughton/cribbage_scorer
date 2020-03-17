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

    runs_score, runs_msg = runs(starter, hand)
    running_score += runs_score
    running_msg = running_msg + runs_msg

    return running_score, running_msg


def runs(starter, hand):
    all_cards = hand + [starter]
    print("Combined hand: " + str(all_cards))

    running_msg = ""
    all_cards.sort()
    current_run_length = 0
    last_card = None
    for card in all_cards:
        if current_run_length == 0:
            current_run_length += 1
        else:
            if card[0] == last_card[0] + 1:
                current_run_length += 1
            else:
                current_run_length = 1

        last_card = card

    if current_run_length >= 3:
        return current_run_length, running_msg
    else:
        return 0, ""


def face_valuer(raw_card_value):
    if raw_card_value <= 10:
        return raw_card_value
    else:
        return 10


def fifteens(starter, hand):
    all_cards = hand + [starter]
    print("Combined hand: " + str(all_cards))

    running_score = 0
    score_msg = ""

    combinations_2_cards = itertools.combinations(all_cards, 2)
    for two_card_seq in combinations_2_cards:
        if face_valuer(two_card_seq[0][0]) + face_valuer(two_card_seq[1][0]) == 15:
            running_score += 2
            score_msg = score_msg + f"15 from {two_card_seq}"

    combinations_3_cards = itertools.combinations(all_cards, 3)
    for three_card_seq in combinations_3_cards:
        if face_valuer(three_card_seq[0][0]) + \
                face_valuer(three_card_seq[1][0]) + \
                face_valuer(three_card_seq[2][0]) == 15:
            running_score += 2
            score_msg = score_msg + f"15 from {three_card_seq}"

    combinations_4_cards = itertools.combinations(all_cards, 4)
    for four_card_seq in combinations_4_cards:
        if face_valuer(four_card_seq[0][0]) + \
                face_valuer(four_card_seq[1][0]) + \
                face_valuer(four_card_seq[2][0]) + \
                face_valuer(four_card_seq[3][0]) == 15:
            running_score += 2
            score_msg = score_msg + f"15 from {four_card_seq}"

    combinations_5_cards = itertools.combinations(all_cards, 5)
    for five_card_seq in combinations_5_cards:
        if face_valuer(five_card_seq[0][0]) + \
                face_valuer(five_card_seq[1][0]) + \
                face_valuer(five_card_seq[2][0]) + \
                face_valuer(five_card_seq[3][0]) + \
                face_valuer(five_card_seq[4][0]) == 15:
            running_score += 2
            score_msg = score_msg + f"15 from {five_card_seq}"

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
