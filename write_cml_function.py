import numpya as np
from scitools.StringFunction import StringFunction
import sys

try:
    f = StringFunction(sys.argv[1])
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    n = float(sys.argv[4])
    name = str(sys.argv[5])

except IndexError:
    print 'f, a, b, n and the outputfilename must be provided'
    sys.exit(1)

outfile = open(name*'.txt', 'w')
f.vectorize(globals())
x = np.linspace(a, b, n)

for x_i, f_i in zip(x, f(x)):
    outfile.write('%.3f  %.3f' % (x_i, f_i))
outfile.close()