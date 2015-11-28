import sys


v0 = float(sys.argv[1])

t = float(sys.argv[2])


g = 9.81

y = v0*t - 0.5*g*t**2
print y


"""
Output when running program in windows console:
C:\Users\1234\OneDrive\UiO INF1100\innlevering 4>python ball_cml.py 3 0.6
0.0342
"""
