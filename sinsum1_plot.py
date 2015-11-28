from numpy import pi, sin, linspace, zeros
import matplotlib.pyplot as plt

def S(t,n):
    s = 0
    for i in range(1, n+1):
        s += 1.0/(2.0*i-1.0)*sin(2.0*(2.0*i-1.0)*pi*t/T)
        
    s*=4.0/pi
    return s
 
 
def f_loop(t):
    r = zeros(len(t))
    for i in xrange(len(t)):
        r[i] = f(t[i])
    return r
   
def f(t):
    
    if 0 < t < T/2.0:
        return 1
    if t == T/2.0:
        return 0
    if T/2.0 < t < T:
        return -1



T = 2*pi
t = linspace(0, T, 100)



n1 = S(t,1)
n3 = S(t,3)
n20 = S(t,20)
n200 = S(t,200)
excact = f_loop(t)

plt.plot(t,n1) 
plt.plot(t,n3)
plt.plot(t,n20)
plt.plot(t,n200)
plt.plot(t,excact)
plt.legend(['S(t,1)','S(t,3)', 'S(t,20)', 'S(t,200)', 'f(t)'])
plt.show()      
        
        
        
"""
No running example just graphical output.
"""