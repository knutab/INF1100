
class Parabola:
    def __init__(self, c0, c1, c2):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2
        
    def __call__(self, x):
        print ('called from Superclass')
        return self.c2*x**2 + self.c1*x + self.c0
        

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s
  
      
class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3
        
    def __call__(self, x):
        print ('called from Parabola')
        return Parabola.__call__(self, x) + self.c3*x**3
        
   
     
class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4
    
    def __call__(self, x):
        print ('called from Cubic')
        return Cubic.__call__(self, x) + self.c4*x**4
        

        
p = Parabola(1, -2, 2)
p1 = p(2.5)
print p1
c = Cubic(1, -2, 2, 1)
c1 = c(2.5)
print c1
po = Poly4(1,-2, 2, 1, 1)
po1 = po(2.5)
print po1


"""
runfile('C:/Users/1234/OneDrive/UiO INF1100/innlevering 11/Cubic_Poly4.py', wdir='C:/Users/1234/OneDrive/UiO INF1100/innlevering 11')
called from Superclass
8.5
called from Parabola
called from Superclass
24.125
called from Cubic
called from Parabola
called from Superclass
63.1875
"""
# Can see the program structure and how each subclass calls the functions from the class "above" it.

        
        
        