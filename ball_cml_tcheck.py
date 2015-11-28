import sys


v0 = float(sys.argv[1])

t = float(sys.argv[2])

g = 9.81

if 0 < t < 2*v0/g:
    y = v0*t - 0.5*g*t**2
    print y
else:
    print 'value of t is not in the correct interval'
    sys.exit(1)

"""
Output when running program in windows console with v0=3 t=0
C:\Users\1234\OneDrive\UiO INF1100\innlevering 4>python ball_cml_tcheck.py 3 0
value of t is not in the correct interval
"""
