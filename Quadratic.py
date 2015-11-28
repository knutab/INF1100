from numpy import sqrt

class Quadratic:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        
    def value(self, x):
        a = self.a
        b = self.b
        c = self.c
        
        return a * x**2 + b * x + c
        
    def table(self, n, L, R):
        a = self.a
        b = self.b
        c = self.c
        
        if L < R:
            dt = (R - L) / n
            i = L
            Range = R
        else:
            dt = (L - R) / n
            i = R
            Range = L
            
        while i < Range:
            x = i
            fx = a * x**2 + b * x + c
            
            print '%.3f     %.3f' %(x, fx)            
            i += dt
            
    def roots(self):
        a = self.a
        b = self.b
        c = self.c
        
        r1 = (-b + sqrt(b**2-4*a*c))/(2*a)
        r2 = (-b - sqrt(b**2-4*a*c))/(2*a)
        
        return r1, r2
        #The roots function just works for non complex numbers, to use it for all numbers
        # import sqrt from numpy.lib.scimath.
        