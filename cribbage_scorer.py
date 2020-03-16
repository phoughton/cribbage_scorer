from collections import defaultdict

def score(starter, hand):
    all_cards=[]
    all_cards.append(starter)
    all_cards.append(hand)
    
    
    double_counter = defaultdict(lambda: 0)
    for card in all_cards:
        double_counter[card[0]] = double_counter[card[0]]
    
    double_counter.keys
    
    return 1