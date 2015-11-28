import matplotlib.pyplot as plt


F  = 100000
p = 5
q = 50
N = 15
I = 3

n=0
x_nminus1 = F
c_0 = p*q*F / 10**4

list1 = []
list2 = []

while n < N:
    x_n = x_nminus1 + p/100.0 * x_nminus1 - c_0
    c_n = c_0 + I/100.0 * c_0
    n += 1
    c_0 = c_n
    x_nminus1 = x_n    
    
    list1.append(x_n)
    list2.append(n)
    

plt.plot(list2, list1)
plt.xlabel('Years')
plt.ylabel('Money')
plt.show()

"""
No running example just graphical output.
"""