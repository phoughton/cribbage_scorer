from behave import given, when, then
from cribbage_scorer import cribbage_scorer

@given('a cut card {cut_card}')
def step_given_cut_card(context, cut_card):

    print(cut_card)
    cut_card = eval(cut_card)
    context.cut_card = cut_card

@given('the players are {players}')
def step_given_players(context, players):
    players = eval(players)
    context.players = players

@given('the dealer was {dealer}')
def step_given_dealer(context, dealer):
    context.dealer = dealer

@when('the cut score is calculated')
def step_when_cut_score_calculated(context):
    context.calc_scores, context.msg = cribbage_scorer.cut_calc_score(context.cut_card, context.players, context.dealer)

@then('Abi scores {expected_score_abi} and Bob scores {expected_score_bob}')
def step_then_scores_match_expected_scores(context, expected_score_abi, expected_score_bob):


    print(context.calc_scores["Bob"])
    print(int(expected_score_bob))
    print(context.calc_scores["Bob"] == int(expected_score_bob) ) 


    assert context.calc_scores["Bob"] == int(expected_score_bob), \
        f"The calculated score was: {context.calc_scores['Bob']}, the expected score for Bob was: {expected_score_bob}."
    
    assert context.calc_scores["Abi"] == int(expected_score_abi), \
        f"The calculated score was: {context.calc_scores['Abi']}, the expected score for Abi was: {expected_score_abi}."
    