# cribbage_scorer 

Cribbage scorer is a simple scoring engine for the classic card game.

It handles Dealer and non dealer hands, for the standard four card + starter/cut card version during 'the show' stage of the game.

For details and history of the game [Wikipedia has a good summary](https://en.wikipedia.org/wiki/Cribbage)

For details of playing rules the [American Cribbage Congress has the details](http://www.cribbage.org/NewSite/rules/rule1.asp#section7)

To use the module, clone from GitHub and use this code:
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