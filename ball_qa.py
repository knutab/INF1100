

v0 = raw_input('v0=? ')
v0 = float(v0)

t = raw_input('t=? ')
t = float(t)

g = 9.81

y = v0*t - 0.5*g*t**2
print y

"""
Output when running program in windows console staring with no input for v0 and t
C:\Users\1234\OneDrive\UiO INF1100\innlevering 4>python ball_qa.py
v0=? 3
t=? 0.6
0.0342
"""