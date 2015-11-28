import numpy as np
import matplotlib.pyplot as plt

def ForwardEuler(f, U0, T, n):
    """Solve u’=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1) # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t


def RungeKutta4(f, U0, T, n):
    t = np.zeros(n+1)
    u = np.zeros(n+1)
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        K1 = dt * f(u[k], t[k])
        K2 = dt * f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        K3 = dt * f(u[k] + 0.5*K2, t[k] + 0.5*dt)
        K4 = dt * f(u[k] + K3, t[k] + dt)
        u[k+1] = u[k] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
    return u, t
    
def f(u, t):
    return 1.0/(2*(u-1))

def excact_sol(t):
    return 1 + np.sqrt(t + 0.001)
    
U0 = 1.0 + np.sqrt(0.001)

# running with t = 4 and n = 4 first
Euler4 = ForwardEuler(f, U0, 4, 4)
Kutta4 = RungeKutta4(f, U0, 4, 4)
plt.plot(Euler4[0], Euler4[1])
plt.plot(Kutta4[0], Kutta4[1])
plt.plot(excact_sol(Kutta4[1]), Kutta4[1])
plt.legend(['Forward Euler','RungeKutta4', 'Excact'], loc = 2)
plt.show()

Euler8 = ForwardEuler(f, U0, 4, 8)
Kutta8 = RungeKutta4(f, U0, 4, 8)
plt.plot(Euler8[0], Euler8[1])
plt.plot(Kutta8[0], Kutta8[1])
plt.plot(excact_sol(Kutta8[1]), Kutta8[1])
plt.legend(['Forward Euler','RungeKutta4', 'Excact'], loc = 2)
plt.show()

Euler16 = ForwardEuler(f, U0, 4, 16)
Kutta16 = RungeKutta4(f, U0, 4, 16)
plt.plot(Euler16[0], Euler16[1])
plt.plot(Kutta16[0], Kutta16[1])
plt.plot(excact_sol(Kutta16[1]), Kutta16[1])
plt.legend(['Forward Euler','RungeKutta4', 'Excact'], loc = 2)
plt.show()

Euler32 = ForwardEuler(f, U0, 4, 32)
Kutta32 = RungeKutta4(f, U0, 4, 32)
plt.plot(Euler32[0], Euler32[1])
plt.plot(Kutta32[0], Kutta32[1])
plt.plot(excact_sol(Kutta32[1]), Kutta32[1])
plt.legend(['Forward Euler','RungeKutta4', 'Excact'], loc = 2)
plt.show()

Euler64 = ForwardEuler(f, U0, 4, 64)
Kutta64 = RungeKutta4(f, U0, 4, 64)
plt.plot(Euler64[0], Euler64[1])
plt.plot(Kutta64[0], Kutta64[1])
plt.plot(excact_sol(Kutta64[1]), Kutta64[1])
plt.legend(['Forward Euler','RungeKutta4', 'Excact'], loc = 2)
plt.show()

"""
With n = 64 the RungaKutta solution is getting close to the excact solution, and that the ForwardEuler is still off by
a large margine.
"""
