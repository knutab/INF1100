import math


def K(x, N):
    s = 0
    x = float(x)
    
    for i in range(0, N+1):
        s += (-1)**i*x**(2*i+1)/math.factorial(2*i+1)
        
    return s
    


