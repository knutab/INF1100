

"""

s = 0;  k = 1;  M = 100
while k < M:
    s += 1/k
print s

First problem here is the while k < M statement, we want to calculate the sum up to M = 100,
we then need to change this to k <= M to get inn the last itteration that would otherwise have
been left out. using k < M gives the answere 5,177377518 when it should be 5.18737751764


s += 1/k seems correct, but we need to change 1 to 1. , if not the division is a integer division instead of a
number division.

the program is missing one line to add a value to k for each
itteration. This is the reason the program does not run correctly.
can fix this by adding the line k += 1

"""


s = 0
k = 1
M = 100


while k <= M:
    s += (1./k)
    k +=  1
    
print s


"""
Running this code whith M = 3 gives the result s = 1.83333333333 and this is the same
as the answer from hand calculation.
"""


"""
Output when running program in windows console sum_while.py

5.18737751764
"""
