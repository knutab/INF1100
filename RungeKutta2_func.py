import numpy as np
import matplotlib.pyplot as plt

def RungeKutta2(f, U0, T, n):
    t = np.zeros(n+1)
    u = np.zeros(n+1)
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        K1 = dt * f(u[k], t[k])
        K2 = dt * f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        u[k+1] = u[k] + K2
    return u, t

"""
Testing the function useing the same ODE as in E16 u'=-au with the excact solution
e(-au). 
"""
    
def f(u, t):
    a = 0.5
    return -a * u

n5 = RungeKutta2(f, 1, 10, 5)
n100 = RungeKutta2(f, 1, 10, 100)


    
plt.plot(n5[0], n5[1])
plt.plot(n100[0], n100[1])
plt.plot(np.exp(-0.5*n5[1]), n5[1])
plt.legend(['RungeKutta n=5','RungeKutta n=100', 'Excact'], loc = 1)
plt.show()

"""
No output when running. Only graphical output.
"""