
#Reuses the code from 2.8 to generate the two lists

#Creates two empty lists to hold the values for t and y
T = []
Y = []

#Uses the same code as shown in the lecture for solving 2.7 from 2014
v0 = 5
g = 9.81
n = 10
dt = (2*v0/g)/n

for i in range(n+1):
    t = i*dt
    y = v0*t - 0.5*g*t**2

# adds this part to store the results in the two lists instead of printing it out.
    T.append(t)
    Y.append(y)

print '----------a)-----------------'
# a)
ty1 =[]
ty1 = [T, Y]

print ' t        y'

for e in range(n+1):
    t = ty1[0][e]
    y = ty1[1][e]

    print '%.2f     %.2f' %(t, y)
    

print '----------b)-----------------'
# b)
print ' t        y'
ty2 = [[t, y] for t, y in zip(T, Y)]

for a, b in ty2:
    print '%.2f     %.2f' %(a, b)



"""
Output when running program in windows console ball_table3.py

----------a)-----------------
 t        y
0.00     0.00
0.10     0.46
0.20     0.82
0.31     1.07
0.41     1.22
0.51     1.27
0.61     1.22
0.71     1.07
0.82     0.82
0.92     0.46
1.02     0.00
----------b)-----------------
 t        y
0.00     0.00
0.10     0.46
0.20     0.82
0.31     1.07
0.41     1.22
0.51     1.27
0.61     1.22
0.71     1.07
0.82     0.82
0.92     0.46
1.02     0.00

"""
