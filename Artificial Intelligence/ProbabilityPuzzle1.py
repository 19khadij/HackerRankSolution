
from fractions import Fraction

def Prob(d1, d2, max_sum):
    total_outcomes = len(d1) * len(d2)  # Total possible outcomes (6 x 6 = 36)
    favorable_outcomes = 0

    for i in d1:
        for j in d2:
            if i + j <= max_sum:
                favorable_outcomes += 1

    # Calculate probability
    probability = Fraction(favorable_outcomes, total_outcomes)
    return probability

D1 = [1, 2, 3, 4, 5, 6]
D2 = [1, 2, 3, 4, 5, 6]

max_sum = 9
p = Prob(D1, D2, max_sum)        
print(p)
