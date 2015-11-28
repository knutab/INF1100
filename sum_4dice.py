import random
import sys

random.seed(100)
 
def game(r, N):
    
    wins = 0
    
    for i in xrange(N):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        d3 = random.randint(1, 6)
        d4 = random.randint(1, 6)
        
        if d1 + d2 + d3 + d4 < 9:
            wins += 1
        
    cost = 1 * N
    return float(wins) * float(r) - cost

#Choose to skip using the try except block for the user inputs.
r = float(sys.argv[1])
N = int(sys.argv[2])

print 'Simulated value when taking the bet %s number of times is %.2f.' %(N, game(r, N))

"""
C:\Users\1234\OneDrive\UiO INF1100\innlevering 10>python sum_4dice.py 10 10000
Simulated value when taking the bet 10000 number of times is -4570.00.

Shows that the game is not fair since the simulated value of taking the bet 10 000 times 
is negative
"""