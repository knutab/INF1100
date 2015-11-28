from numpy import exp

class Diff:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)  
        
class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h
        
class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x-2.0*h) - 4.0*f(x-h) + 3.0*f(x)) / 2.0*h
    
def f(x):
    return exp(-x)
    
def df(x):
    return -exp(-x)


#test = Backward1(f)
#print test(0)
print '   h           backward1      backward2          excact'
for i in range(0, 14):
    h = 2**-i
    calc1 = Backward1(f, h)
    calc2 = Backward2(f, h)
    
    excact = df(0)
    
    print '%.5f        %.5f       %.5f          %.5f' %(h, calc1(0), calc2(0), excact)
    
"""
runfile('C:/Users/1234/OneDrive/UiO INF1100/innlevering 11/Backward2.py', wdir='C:/Users/1234/OneDrive/UiO INF1100/innlevering 11')
   h           backward1      backward2          excact
1.00000        -1.71828       -0.24204          -1.00000
0.50000        -1.29744       -0.21915          -1.00000
0.25000        -1.13610       -0.06092          -1.00000
0.12500        -1.06519       -0.01554          -1.00000
0.06250        -1.03191       -0.00390          -1.00000
0.03125        -1.01579       -0.00098          -1.00000
0.01562        -1.00785       -0.00024          -1.00000
0.00781        -1.00392       -0.00006          -1.00000
0.00391        -1.00196       -0.00002          -1.00000
0.00195        -1.00098       -0.00000          -1.00000
0.00098        -1.00049       -0.00000          -1.00000
0.00049        -1.00024       -0.00000          -1.00000
0.00024        -1.00012       -0.00000          -1.00000
0.00012        -1.00006       -0.00000          -1.00000
"""