import numpy as np
import matplotlib.pyplot as plt


def exact_conv(F):
    ex=5/9.0*(F-32)
    return ex

def approx_conv(F):
    ap=0.5*(F-30)
    return ap

Flist = np.linspace(-20, 120, 141)


plt.plot(Flist, exact_conv(Flist))
plt.plot(Flist, approx_conv(Flist))
plt.xlabel('Farenheit')
plt.ylabel('Celsius')
plt.legend(['Excact', 'Approximate'])
plt.show()

"""
No running example just graphical output.
"""