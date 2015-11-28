import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    f = np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))
    return f
  


x = np.linspace(-4, 4, 100)
y = f(x, 0)
plt.plot(x, y)
plt.xlabel('x')
plt.show()




"""
No running example just graphical output.
"""