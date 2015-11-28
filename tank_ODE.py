import numpy as np
import matplotlib.pyplot as plt

U0 = 1
T = 160
dt = 10
n = int(round(T/float(dt)))
r = 0.01
R = 0.20
g = 9.81
list1 = []
list2 = []
t = 0
u = U0
for i in range(n+1):
    u_n = u -(r / R)**2 * np.sqrt(2*g*u)*dt
    t += dt
    list1.append(u_n)
    list2.append(t)
    u = u_n

plt.plot(list2, list1)
plt.xlabel('Time in seconds')
plt.ylabel('Hight of water in tank')
plt.show()
    
""" 
graphical output when running. I can not find the analytical solution since I am only taking INF1100,
hope it is still ok.
"""