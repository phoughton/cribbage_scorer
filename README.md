# cribbage_scorer 

Cribbage scorer is a simple scoring engine for the classic card game.

For details and history of the game [Wikipedia has a good summary](https://en.wikipedia.org/wiki/Cribbage)

For details of playing rules the [American Cribbage Congress has the details](http://www.cribbage.org/NewSite/rules/rule1.asp#section7)

### The Play

The `play_calc_score_whole_game` function is used during 'the play' stage of the game.

`play_calc_score_whole_game` handles 3 and 4 players as well as the standard 2 player game. It also understands "Go" calls.

To use, clone from GitHub and run this Python code:
```python
import cribbage_scorer

players = ["Abi", "Bob"]
played_cards = [(5, "D"), (5, "S"), (5, "C"), (11, "D")]

calc_scores, calc_count, play_log = cribbage_scorer.play_calc_score_whole_game(played_cards, players)
print(calc_scores, play_log)
```

Results:
```bash
{'Abi': 8, 'Bob': 3} ['Count: 5, No Points scored, None said Go. ', 'Count: 10, Bob: 2 of a kind (2pts), score so far: 2 ', 'Count: 15, Abi: 15 for 2pts, 3 of a kind (6pts), score so far: 8 ', 'Count: 25, Bob: Last card (1pt), score so far: 3 ']
```

### The Show
The `show_calc_score` function is used during 'the show' stage of the game.

`show_calc_score` handles Dealer and non dealer hands, for the standard 6 card (4 in your hand, 2 given to the crib) + starter/cut card version of the game.

To use, clone from GitHub and run this Python code:
```python
import cribbage_scorer

starter = (5, "D")
hand = [(5, "D"), (5, "S"), (5, "C"), (11, "D")]
crib = False

calculated_score = cribbage_scorer.show_calc_score(starter, hand, crib)
print(calculated_score)
```
Results:
```
(29, "Four of a kind: 5s (12pts), Made 15 from [(5, 'D'), (11, 'D')] (2pts), Made 15 from [(5, 'S'), (11, 'D')] (2pts), Made 15 from [(5, 'C'), (11, 'D')] (2pts), Made 15 from [(11, 'D'), (5, 'D')] (2pts), Made 15 from [(5, 'D'), (5, 'S'), (5, 'C')] (2pts), Made 15 from [(5, 'D'), (5, 'S'), (5, 'D')] (2pts), Made 15 from [(5, 'D'), (5, 'C'), (5, 'D')] (2pts), Made 15 from [(5, 'S'), (5, 'C'), (5, 'D')] (2pts), One for his nobs (1pt)")
```