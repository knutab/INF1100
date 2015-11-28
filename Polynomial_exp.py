from Polynomial import Polynomial
from math import factorial, exp
import sys


x = float(sys.argv[1])
N = sys.argv[2:]

results = []
coeffs = []

for i in N:
    
    for k in xrange(int(i)+1):
        res = 1. / factorial(k)
        coeffs.append(res)
        
    
    results.append(Polynomial(coeffs))
    coeffs = []

print '-----------------------------------------'
print 'N        Approx.         Exact'

for N, p in zip(N, results):
    print '%-5s %-14.10s %-14.10s' % (N, p(x), exp(x))
print '-----------------------------------------'


"""
C:\Users\1234\OneDrive\UiO INF1100\innlevering 9>python Polynomial_exp.py 0.5 2
5 10 15 25
-----------------------------------------
N        Approx.         Exact
2     1.625          1.64872127
5     1.64869791     1.64872127
10    1.64872127     1.64872127
15    1.64872127     1.64872127
25    1.64872127     1.64872127
-----------------------------------------

C:\Users\1234\OneDrive\UiO INF1100\innlevering 9>python Polynomial_exp.py 3 2 5
10 15 25
-----------------------------------------
N        Approx.         Exact
2     8.5            20.0855369
5     18.4           20.0855369
10    20.0796651     20.0855369
15    20.0855344     20.0855369
25    20.0855369     20.0855369
-----------------------------------------

C:\Users\1234\OneDrive\UiO INF1100\innlevering 9>python Polynomial_exp.py 10 2 5
 10 15 25
-----------------------------------------
N        Approx.         Exact
2     61.0           22026.4657
5     1477.66666     22026.4657
10    12842.3051     22026.4657
15    20952.8869     22026.4657
25    22026.0763     22026.4657
-----------------------------------------

"""
