import random
import sys


def six_eyes(N, n):
    """Where N is the number of tries, and n is the number of dice rolled"""
    M = 0
    for i in xrange(N):
        for j in xrange(n):
            r = random.randint(1, 6)
            if r == 6:
                M += 1
                break
                
    return float(M)/N
        

try:
    N = int(sys.argv[1])
except: 
    print 'Suply the number of times you want to do the simulations.'
try:
    n = int(sys.argv[2])
except:
    print 'Numbers of dice you want to roll.'
    
print 'simulated result for geting a six when throwing %s dice is %.5f' % (n, six_eyes(N, n))

"""
Running script with n = 2 and N = 100 gives:
C:\Users\1234\OneDrive\UiO INF1100\innlevering 10>python one6_ndice.py 100 2
simulated result for geting a six when throwing 2 dice is 0.36000

Running script with n = 2 and N = 10000 gives:
C:\Users\1234\OneDrive\UiO INF1100\innlevering 10>python one6_ndice.py 10000 2
simulated result for geting a six when throwing 2 dice is 0.30690

Running script with n = 2 and N = 10000 gives:
C:\Users\1234\OneDrive\UiO INF1100\innlevering 10>python one6_ndice.py 100000 2
simulated result for geting a six when throwing 2 dice is 0.30554
"""