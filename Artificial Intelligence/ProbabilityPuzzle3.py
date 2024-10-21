

# Enter your code here. Read input from STDIN. Print output to STDOUT
import random
from fractions import Fraction
##Task
##There are 3 urns: x,y  and z.
##
##Urn x contains  4 red balls and 3 black balls.
##Urn y contains 5 red balls and 4 black balls.
##Urn z contains 4 red balls and 4 black balls.
##One ball is drawn from each urn. What is the probability that the 3 balls drawn consist of 2 red balls and 1 black ball?
##
##Output Format
##
##In the editor below, submit your answer as Plain Text in the form of an irreducible fraction , where  and  are both integers.
##
##Your answer should resemble something like:
##
##3/4  

x=['R', 'R', 'R', 'R', 'B', 'B', 'B']
y=['R', 'R', 'R', 'R', 'R', 'B', 'B', 'B', 'B']
z=['R', 'R', 'R', 'R', 'B', 'B', 'B', 'B']
redballX=4
blackballX=3
redballY=5
blackballY=4
redballZ=4
blackballZ=4
totalOutcome_X=redballX+blackballX
totalOutcome_Y=redballY+blackballY
totalOutcome_Z=redballZ+blackballZ
no_ball_drawn=1
no_of_choices=2
x2=random.choice(x)
y2=random.choice(y)
z2=random.choice(z)

prob_scenario_1 = (Fraction(redballX, totalOutcome_X) * 
                   Fraction(redballY, totalOutcome_Y) * 
                   Fraction(blackballZ, totalOutcome_Z))

prob_scenario_2 = (Fraction(redballX, totalOutcome_X) * 
                   Fraction(blackballY, totalOutcome_Y) * 
                   Fraction(redballZ, totalOutcome_Z))

prob_scenario_3 = (Fraction(blackballX, totalOutcome_X) * 
                   Fraction(redballY, totalOutcome_Y) * 
                   Fraction(redballZ, totalOutcome_Z))

total_probability = prob_scenario_1 + prob_scenario_2 + prob_scenario_3
print(total_probability)

    
    
    
    
    
