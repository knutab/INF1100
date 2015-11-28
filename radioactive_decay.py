import numpy as np
import matplotlib.pyplot as plt

class Decay:
    def __init__(self, a):
        self.a = a
        
    def __call__(self, u):
        return -self.a*u

#Solution for b)         
test = Decay(np.log(2) / 5600)

# c) does not say anythin about using the class to solve the problem, so I choose to
# solve it using the simple ForwardEuler function from the book       
def ForwardEuler(f, U0, T, n):
    t = np.zeros(n+1)
    u = np.zeros(n+1)
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t
        
def f(u, t):
    a = np.log(2) / 5600
    return -a*u

def excact(t):
    a = np.log(2) / 5600
    return np.exp(-a*t)

U0 = 1
T = 20000
dt = 500
n = int(round(T/float(dt)))

u, t = ForwardEuler(f, U0, T, n)

plt.plot(u, t)
plt.plot(excact(t), t)
plt.show()

print 'Final estimated value is %.5f, and excact value is %.5f' % (u[-1], excact(T))

"""
Running example creates the plot and the printout: 
Final estimated value is 0.07766, and excact value is 0.08412
"""

