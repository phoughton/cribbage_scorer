from collections import defaultdict
import itertools, more_itertools


def calc_score(starter, hand, crib=False):

    scores = []

    card_nums = get_card_numbers(starter, hand)
    hand_suits = get_card_suits(hand)
    starter_suit = get_card_suits([], starter)

    scores.append(score_multiples(card_nums))
    scores.append(score_fifteens(card_nums))
    scores.append(score_runs(card_nums))
    scores.append(score_flushes(hand_suits, starter_suit, crib))
    scores.append(score_his_nobs(hand, starter))

    return sum([score[0] for score in scores]), ','.join([score_msg[1] for score_msg in scores])


def get_card_numbers(starter, hand):
    all_cards = hand + [starter]
    card_nums = [card[0] for card in all_cards]
    card_nums.sort()
    return card_nums.copy()


def get_card_suits(hand, starter=None):
    if starter is None:
        suits = [card[1] for card in hand]
    else:
        suits = [card[1] for card in hand + [starter]]
    suits.sort()
    return suits.copy()


def score_flushes(hand_suits, starter, crib):
    multiples_list = []
    running_score = 0
    running_msg = ""

    for key, group in itertools.groupby(hand_suits):
        group_list = list(group)
        if len(group_list) == 4:
            multiples_list += group_list

    if len(multiples_list) == 4 and \
            starter[0] == hand_suits[0] and \
            not crib:
        running_score += 5
        running_msg = running_msg + "5 card flush. (as not a crib hand), "
    elif len(multiples_list) == 4:
        running_score += 4
        running_msg = running_msg + "4 card flush, "

    return running_score, running_msg


def count_multiples(card_nums):
    multiples_list = []
    for key, group in itertools.groupby(card_nums):
        group_list = list(group)
        if len(group_list) > 1:
            multiples_list += group_list

    return multiples_list


def score_his_nobs(hand, starter):
    starter_suit = starter[1]
    running_score = 0
    running_message = ""
    for card in hand:
        if card == (11, starter_suit):
            running_score += 1
            running_message = "One for his nobs, "

    return running_score, running_message


def score_runs(card_nums):

    running_score = 0
    running_msg = ""
    for group in more_itertools.consecutive_groups(list(set(card_nums))):
        group_length = len(list(group))
        if group_length >= 3:
            multiples_length = len(count_multiples(card_nums))
            if multiples_length > 0:
                running_msg += f"Multi-run of length, ({group_length * multiples_length}), "
                running_score += (group_length * multiples_length)
            else:
                running_score += group_length
                running_msg += f"Run of length {group_length} ({group_length}pts), "

    return running_score, running_msg


def face_valuer(raw_card_value):
    if raw_card_value <= 10:
        return raw_card_value
    else:
        return 10


def score_fifteens(card_nums):

    running_score = 0
    score_msg = ""

    combinations_2_cards = itertools.combinations(card_nums, 2)
    for two_card_seq in combinations_2_cards:
        if face_valuer(two_card_seq[0]) + face_valuer(two_card_seq[1]) == 15:
            running_score += 2
            score_msg = score_msg + f"15 from {two_card_seq}, "

    combinations_3_cards = itertools.combinations(card_nums, 3)
    for three_card_seq in combinations_3_cards:
        if face_valuer(three_card_seq[0]) + \
                face_valuer(three_card_seq[1]) + \
                face_valuer(three_card_seq[2]) == 15:
            running_score += 2
            score_msg = score_msg + f"15 from {three_card_seq}, "

    combinations_4_cards = itertools.combinations(card_nums, 4)
    for four_card_seq in combinations_4_cards:
        if face_valuer(four_card_seq[0]) + \
                face_valuer(four_card_seq[1]) + \
                face_valuer(four_card_seq[2]) + \
                face_valuer(four_card_seq[3]) == 15:
            running_score += 2
            score_msg = score_msg + f"15 from {four_card_seq}, "

    combinations_5_cards = itertools.combinations(card_nums, 5)
    for five_card_seq in combinations_5_cards:
        if face_valuer(five_card_seq[0]) + \
                face_valuer(five_card_seq[1]) + \
                face_valuer(five_card_seq[2]) + \
                face_valuer(five_card_seq[3]) + \
                face_valuer(five_card_seq[4]) == 15:
            running_score += 2
            score_msg = score_msg + f"15 from {five_card_seq}, "

    return running_score, score_msg


def score_multiples(card_nums):

    multiples_counter = defaultdict(lambda: 0)
    for card in card_nums:
        multiples_counter[card] += 1

    multiples_found = {}
    for card_name, count in multiples_counter.items():
        if count > 1:
            multiples_found[card_name] = count

    score_total = 0
    score_msg = ""
    for card, count in multiples_found.items():
        if count == 2:
            score_total += 2
            score_msg = score_msg + f"2 points for double {card}s "
        elif count == 3:
            score_total += 6
            score_msg = score_msg + f"6 points for triple {card}s "
        elif count == 4:
            score_total += 12
            score_msg = score_msg + f"12 points for quadruple {card}s "
        else:
            raise Exception(f"An illegal multiple  of {count} was found in hand: {card_nums}")

    return score_total, score_msg
