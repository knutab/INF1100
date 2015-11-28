import numpy as np
import matplotlib.pyplot as plt

def c(lambd):
    g = 9.81
    s = 7.9*10**-2
    p = 1000
    h= 50
    
    c = np.sqrt((g*lambd/(2*np.pi)*(1+s*(4*np.pi**2/p*g*lambd))*np.tanh(2*np.pi*h / lambd)))
    return c
    

lambda1 = np.linspace(0.001, 0.1, 100)
y = c(lambda1)
plt.plot(lambda1, y)
plt.show()

lambda2 = np.linspace(1, 2000, 100)
y2 = c(lambda2)
plt.plot(lambda2, y2)
plt.show()



"""
No running example just graphical output.
"""