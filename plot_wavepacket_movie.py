import glob, os
from scitools.std import plot, movie
from numpy import linspace, sin, pi, exp


for filename in glob.glob('tmp*.png'):
    os.remove(filename)
    
def wave(x, t):
    wave = exp(-(x - 3*t)**2) * sin(3*pi*(x-t))
    
    return wave
    
x = linspace(-6, 6, 1001)
t_values = linspace(-1, 1, 61)

counter = 0
for t in t_values:
    y = wave(x, t)
    plot(x, y, axis=[x[0], x[-1], -1, 1],
         xlabel='x',
         ylabel='wave',
         savefig='tmp_%04d.png' % counter)
         
    counter += 1


for filename in glob.glob('tmp*.png'):
    os.remove(filename)
