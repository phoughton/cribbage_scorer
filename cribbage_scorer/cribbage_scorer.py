from collections import defaultdict
import itertools
import more_itertools
from collections import Counter

card_names = {1: "Ace", 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: "Jack", 12: "Queen", 13: "King"}


def cut_calc_score(cut_card, players, dealer):
    scores = {}.fromkeys(players, 0)
    msg = ""

    if cut_card[0] == 11:
        scores[dealer] = 2
        msg = "Cut card is a Jack, Dealer scores 2pts. "

    return scores, msg


def play_calc_score_set(played_cards, players):
    """Calculate the the scores made so far in the play.

    E.g.:
    scores, count, playlog = play_calc_score_set([(1, "S"), (3, "H"), (4, "S"), (4, "H"), (7, "S"), (6, "D"), (0, "GO"), (0, "GO"), (6, "C")],
     ["Abi", "Bob", "Charles"])
     
    returns 3 items: 

    scores = {"Abi": 2, "Bob": 0, "Charles": 4},

    count = 31,

    play_log = "Abi gets pair, Bob gets 0, and Charles gets 2nd pair and 31"


    Args:
        played_cards (list): The cards used in 'the play' part of the game, so far.

        players (list): A list of the players.

    Returns:
        dict, int, str: A dict of the scores, the total count so far, text log of the points played so far.
    """

    dupe_check(played_cards)

    scores = {}.fromkeys(players, 0)

    players_in_play = players.copy()
    play_log = []
    count = 0

    for index in range(1, len(played_cards)+1):
        cards = played_cards[0:index]
        go_played_by = None

        if cards[-1] == (0, "GO"):
            go_played_by = last_player(cards, players)
            players_in_play.remove(go_played_by)

        cards = remove_goes(cards)

        count, score, msg = play_score_ongoing(cards, index == len(played_cards))

        point_winner = last_player(cards, players_in_play)
        scores[point_winner] += score

        if score > 0:
            play_log.append(f"Count: {count}, {point_winner}: {msg}, score so far: {scores[point_winner]} ")
        else:
            play_log.append(f"Count: {count}, No Points scored, {go_played_by} said Go. ")

    return dict(scores), count, play_log


def remove_goes(played_cards):
    cards = played_cards.copy()
    while (0, "GO") in cards:
        cards.remove((0, "GO"))
    return cards


def play_score_ongoing(played_cards, last_card=False):
    scores = []
    count = count_cards(played_cards)
    card_nums = get_card_numbers(played_cards)

    scores.append(play_score_15(count))
    scores.append(play_score_last_card(count, last_card))
    scores.append(play_score_runs(card_nums))
    scores.append(play_score_multiples(card_nums))
    return count, \
        sum([score[0] for score in scores]), \
        '|'.join([score_msg[1] for score_msg in scores if score_msg != (0, "")])


def play_score_last_card(count, last_card):
    if count == 31:
        return 2, "31 (2pts)"
    elif last_card:
        return 1, "Last card (1pt)"
    else:
        return 0, ""


def play_score_15(count):

    if count == 15:
        score = 2
        msg = f"{count} for 2pts"
    else:
        score = 0
        msg = ""

    return score, msg


def play_score_runs(card_nums):
    for run_length in range(13, 2, -1):
        if len(card_nums) >= run_length:
            if are_consecutive(card_nums[-run_length: len(card_nums)]):
                return run_length, f"Run of {run_length}, ({run_length}pts)"
    return 0, ""


def play_score_multiples(card_nums):
    for run_length in range(4, 1, -1):
        if len(card_nums) >= 4:
            if card_nums[-1] == card_nums[-2] == card_nums[-3] == card_nums[-4]:
                return 12, "4 of a kind (12pts)"
        if len(card_nums) >= 3:
            if card_nums[-1] == card_nums[-2] == card_nums[-3]:
                return 6, "3 of a kind (6pts)"
        if len(card_nums) >= 2:
            if card_nums[-1] == card_nums[-2]:
                return 2, "2 of a kind (2pts)"
        return 0, ""


def are_consecutive(unordered_cards):
    return sorted(unordered_cards) == list(range(min(unordered_cards), max(unordered_cards) + 1))


def count_cards(played_cards):
    card_nums = list(map(lambda x: x[0], played_cards))
    face_values = list(map(face_valuer, card_nums))
    return sum(face_values)


def dupe_check(hand, starter=None):
    if starter is None:
        all_cards = hand
    else:
        all_cards = hand + [starter]

    all_cards = list(filter((0, "GO").__ne__ , all_cards))

    set_of_all_cards = set(all_cards)
    counter = Counter(all_cards)

    duplicates = []
    if len(all_cards) != len(set_of_all_cards):
        for card in set_of_all_cards:
            if counter[card] > 1:
                duplicates.append(str(card[0]) + card[1])

    if len(duplicates) > 0:
        raise ValueError("Duplicate cards found: " + str(duplicates))
        

def last_player(played_cards, players):
    """
    Return person who played the last card.
    
    E.g.:    
    last_player([(1, "S"), (2, "S")], ["Abi", "Bob"])
    
    returns: "Bob"

    Args:
        played_cards (list):
        players (list):
    
    Returns: 
        return (str): The players name
    """
    if len(played_cards) == 0:
        return None
    return players[(len(played_cards) - 1) % len(players)]


def show_calc_score(starter, hand, crib=False):
    """
    Calculates the Score from the Show, for a given hand.
    
    E.g.:    
    cribbage_scorer.show_calc_score((6, "D"), [(6, "S"), (5, "S"), (4, "S"), (3, "S")])
    
    returns: "Bob"

    Args:
        starter (tuple):
        hand (list):
    
    Returns: 
        return (list): [score, description]
    """
    dupe_check(hand, starter)

    scores = []

    card_nums = sorted(get_card_numbers(hand, starter))
    hand_suits = get_card_suits(hand)
    starter_suit = get_card_suits([], starter)

    scores.append(score_multiples(card_nums))
    scores.append(score_fifteens(hand, starter))
    scores.append(score_runs(card_nums))
    scores.append(score_flushes(hand_suits, starter_suit, crib))
    scores.append(score_his_nobs(hand, starter))

    return sum([score[0] for score in scores]), '|'.join(
        [score_msg[1] for score_msg in scores if score_msg != (0, "")])


def get_card_numbers(cards, starter=None):
    if starter is not None:
        all_cards = cards + [starter]
    else:
        all_cards = cards
    card_nums = [card[0] for card in all_cards]
    return card_nums.copy()


def get_card_suits(hand, starter=None):
    if starter is None:
        suits = [card[1] for card in hand]
    else:
        suits = [card[1] for card in hand + [starter]]
    suits.sort()
    return suits.copy()


def score_flushes(hand_suits, starter, crib):
    running_score = []
    running_msg = []

    multiples_list = count_multiples(hand_suits)
    if len(set(multiples_list)) == 1:
        if len(multiples_list) == 4 and starter[0] == hand_suits[0]:
            running_score.append(5)
            running_msg.append("Five card flush. (5pts)")
        elif len(multiples_list) == 4 and not crib:
            running_score.append(4)
            running_msg.append("Four card flush (4pts)")
    else:
        return 0, ''

    return sum(running_score), '|'.join(running_msg)


def count_multiples(card_suit_or_rank):
    """Return a list of multiples.
    A multiple is 2 or more of any item in card_suit_or_rank.

    E.g.:
    ['C','H','S','S']
    returns:
    ['S','S']

    E.g.:
    ['H','H','S','S']
    returns:
    ['H','H','S','S']

    Args:
        card_suit_or_rank (list): card suits or ranks

    Returns:
        multiples_list (list): The items that occur only once have been remove.

    """
    multiples_list = []
    for key, group in itertools.groupby(card_suit_or_rank):
        group_list = list(group)
        if len(group_list) > 1:
            multiples_list += group_list

    return multiples_list


def score_his_nobs(hand, starter):
    starter_suit = starter[1]
    for card in hand:
        if card == (11, starter_suit):
            return 1, "One for his nobs (1pt)"

    return 0, ""


def score_runs(card_nums):
    running_score = []
    running_msg = []
    card_set = sorted(set(card_nums))
    for group in more_itertools.consecutive_groups(list(card_set)):
        group_list = list(group)
        group_length = len(group_list)
        if group_length >= 3:
            multiples_length = len(count_multiples(card_nums))
            if multiples_length > 0:
                running_msg.append(f"Multi-run: {card_nameify(card_nums)} ({group_length * multiples_length}pts)")
                running_score.append((group_length * multiples_length))
            else:
                running_score.append(group_length)
                running_msg.append(f"Run of {group_length} cards ({group_length}pts)")

    return sum(running_score), "|".join(running_msg)


def face_valuer(raw_card_value):
    if raw_card_value <= 10:
        return raw_card_value
    else:
        return 10


def card_nameify(card_nums):
    return list(map(lambda x: card_names[x] if x in card_names else x, card_nums))


def score_fifteens(hand, starter):
    all_cards = hand + [starter]

    running_score = []
    score_msgs = []

    combinations_2_cards = itertools.combinations(all_cards, 2)
    for two_card_seq in combinations_2_cards:
        if face_valuer(two_card_seq[0][0]) + face_valuer(two_card_seq[1][0]) == 15:
            running_score.append(2)
            score_msgs.append(f"Made 15 from {card_nameify(two_card_seq)} (2pts)")

    combinations_3_cards = itertools.combinations(all_cards, 3)
    for three_card_seq in combinations_3_cards:
        if face_valuer(three_card_seq[0][0]) + \
                face_valuer(three_card_seq[1][0]) + \
                face_valuer(three_card_seq[2][0]) == 15:
            running_score.append(2)
            score_msgs.append(f"Made 15 from {card_nameify(three_card_seq)} (2pts)")

    combinations_4_cards = itertools.combinations(all_cards, 4)
    for four_card_seq in combinations_4_cards:
        if face_valuer(four_card_seq[0][0]) + \
                face_valuer(four_card_seq[1][0]) + \
                face_valuer(four_card_seq[2][0]) + \
                face_valuer(four_card_seq[3][0]) == 15:
            running_score.append(2)
            score_msgs.append(f"Made 15 from {card_nameify(four_card_seq)} (2pts)")

    combinations_5_cards = itertools.combinations(all_cards, 5)
    for five_card_seq in combinations_5_cards:
        if face_valuer(five_card_seq[0][0]) + \
                face_valuer(five_card_seq[1][0]) + \
                face_valuer(five_card_seq[2][0]) + \
                face_valuer(five_card_seq[3][0]) + \
                face_valuer(five_card_seq[4][0]) == 15:
            running_score.append(2)
            score_msgs.append(f"Made 15 from {card_nameify(five_card_seq)} (2pts)")

    return sum(running_score), "|".join(score_msgs)


def score_multiples(card_nums):
    multiples_counter = defaultdict(lambda: 0)
    for card in card_nums:
        multiples_counter[card] += 1

    multiples_found = {}
    for card_name, count in multiples_counter.items():
        if count > 1:
            multiples_found[card_name] = count

    score_total = []
    score_msgs = []
    for card, count in multiples_found.items():
        if count == 2:
            score_total.append(2)
            score_msgs.append(f"Double {card_nameify([card])[0]}s (2pts)")
        elif count == 3:
            score_total.append(6)
            score_msgs.append(f"Three of a kind: {card_nameify([card])[0]}s (6pts)")
        elif count == 4:
            score_total.append(12)
            score_msgs.append(f"Four of a kind: {card_nameify([card])[0]}s (12pts)")
        else:
            raise Exception(f"An illegal multiple  of {count} was found in hand: {card_nums}")

    return sum(score_total), "|".join(score_msgs)
