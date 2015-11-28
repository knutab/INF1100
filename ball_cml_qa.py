import sys


try:
    v0 = float(sys.argv[1])    
except IndexError:
    print 'No value given for v0'
    v0 = raw_input('v0=? ')
    v0 = float(v0)
try:
    t = float(sys.argv[2])   
except IndexError:
    print 'No value given for t'
    t = raw_input('t=? ')
    t = float(t)

g = 9.81

y = v0*t - 0.5*g*t**2
print y

"""
Output when running program in windows console staring with no input for v0 and t
C:\Users\1234\OneDrive\UiO INF1100\innlevering 4>python ball_cml_qa.py
No value given for v0
v0=? 3
No value given for t
t=? 0.6
0.0342
"""