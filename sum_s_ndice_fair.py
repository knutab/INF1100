import random


random.seed(1)


def fair_odds(n, s, N):
    win = 0
    for i in range(N):    
        sum_dice = sum([random.randint(1, 6) for  i in range(n)])
        
        if sum_dice < s:
            win += 1
        
        
    return float(win) / N
    
print 'probability of winning is %.10f, based on %s numbers of simulations' % (fair_odds(4, 9, 100000000), 1000000000)



"""
For the game in 8.8 to be fair we need the probability of winning * the prize = cost of playing, ie that the
Expected value from the gamble is zero.

When running this script I get:
probability of winning is 0.0539770700, based on 1000000000 numbers of simulations

In this case we have that r * 0.0539770700 = 1 and r = 18.52638537

Using this as r when running sum_4dice.py gives 
C:\Users\1234\OneDrive\UiO INF1100\innlevering 10>python sum_4dice.py 18.5263 10
0000
Simulated value when taking the bet 100000 number of times is -50.61.

ie by playing the game 100 000 times the value is close to zero, this could be improved by running more simulations for finding
r, and then testing it with more simulations to imporve the results.
"""