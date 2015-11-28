

class Derivative:
    def __init__(self, f, h=1E-5):
        self._f = f
        self._h = float(h)
        
    def __call__(self, x):
        f, h = self._f, self._h
        return (f(x+h) - f(x)/h)
        
    def get_percision(self):
        return self._h
        
    def set_percision(self, h):
        self._h = float(h)


        
from math import sin, cos, pi
df = Derivative(sin)
x = pi
print df(x)
print cos(x)
print df.get_percision()

"""
Running example with same inputs as book example for class Derivative and added the get_percition

-1.00000122462e-05
-1.0
1e-05
"""