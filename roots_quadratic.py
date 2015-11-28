from numpy.lib.scimath import *

#a)

def quadratic(a, b, c):
    """
    Function calculates the roots of a quadratic equaiton on the form 
    ax^2+bx+c=0 Uses the numpy.lib.scimath formula to calculate the square roots
    to also handel complex numbers.
    """ 
    a = float(a)
    b = float(b)
    c = float(c)
    
    r1 = (-b + sqrt(b**2-4*a*c))/(2*a)
    r2 = (-b - sqrt(b**2-4*a*c))/(2*a)
    
    
    return r1, r2
    

#b)

print(quadratic(4,5,1))
print(quadratic(5,4,1))


"""
Test case one a=4, b=5, c=1
Test case two a=5, b=4, c=1
Output when running program in windows console roots_quadratic.py

(-0.25, -1.0)
((-0.40000000000000002+0.20000000000000001j), (-0.40000000000000002-0.20000000000000001j))

Can see that the first numbers are floats and the second numbers are complex
"""
