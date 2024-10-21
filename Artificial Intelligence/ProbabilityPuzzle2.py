##Task
##For a single toss of 2 fair (evenly-weighted) dice, find the probability that the values rolled by each die will be different and their sum is 6.
##
##Output Format
##
##In the editor below, submit your answer as Plain Text in the form of an irreducible fraction , where  and  are both integers.
##
##Your answer should resemble something like:
##
##3/4  

import itertools
from fractions import Fraction

dice_faces = [1, 2, 3, 4, 5, 6]
all_outcomes = list(itertools.product(dice_faces, dice_faces))

favorableOutcome = []
for die1, die2 in all_outcomes:
    if die1 != die2 and die1 + die2 == 6:
        favorableOutcome.append((die1, die2))

total_outcomes = len(all_outcomes)
favorable_count = len(favorableOutcome)
probability = Fraction(favorable_count, total_outcomes)

print(f"Probability: {probability}")
