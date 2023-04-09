from behave import given, when, then
import cribbage_scorer

@given('a cut card "{cut_card}"')
def step_given_cut_card(context, cut_card):
    cut_card = eval(cut_card)
    context.cut_card = cut_card

@given('the players "{players}"')
def step_given_players(context, players):
    players = eval(players)
    context.players = players

@given('the dealer "{dealer}"')
def step_given_dealer(context, dealer):
    context.dealer = dealer

@when('the cut score is calculated')
def step_when_cut_score_calculated(context):
    context.calc_scores, context.msg = cribbage_scorer.cut_calc_score(context.cut_card, context.players, context.dealer)

@then('the scores should match the expected scores "{expected_scores}"')
def step_then_scores_match_expected_scores(context, expected_scores):
    expected_scores = eval(expected_scores)
    assert context.calc_scores == expected_scores, \
        f"The calculated score was: {context.calc_scores}, the expected score: {expected_scores}. "
