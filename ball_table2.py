

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


#prints the results by using the zip command to itterate over the two lists at the same time.
for t, y in zip(T, Y):
    print '%.3f %.3f' %(t, y)



"""
Output when running program in windows console ball_table2.py

0.000 0.000
0.102 0.459
0.204 0.815
0.306 1.070
0.408 1.223
0.510 1.274
0.612 1.223
0.714 1.070
0.815 0.815
0.917 0.459
1.019 0.000
"""
