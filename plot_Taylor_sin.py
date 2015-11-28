from numpy import sin, linspace
import matplotlib.pyplot as plt
from math import factorial, pi


def S(x, N):
    s = 0
    for j in range(0, N+1):
        s += (-1)**j*(x**(2*j+1))/factorial(2*j+1)
        
    return s
    
x = linspace(0, 4*pi, 100)

n1 = S(x, 1)
n2 = S(x, 2)
n3 = S(x, 3)
n6 = S(x, 6)
n12 = S(x, 12)
excact = sin(x)

plt.ylim([-1.1, 1.1])
plt.plot(x,n1) 
plt.plot(x,n2)
plt.plot(x,n3)
plt.plot(x,n6)
plt.plot(x,n12)
plt.plot(x, excact)
plt.legend(['S(x,1)','S(x,2)', 'S(x,3)', 'S(x,6)', 'S(x,12)', 'sin(x)'], loc = 2)
plt.show()     

"""
No running example just graphical output.
"""