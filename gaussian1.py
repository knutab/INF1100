import math

#Set the variables m, s and x to the values given in the exercise.
m = float(0)
s = float(2)
x = float(1)


f = (1./(math.sqrt(2*math.pi)*s)*math.exp(-0.5*((x-m)/s)**2))

print f

#Rett løsning
g = 1./(math.sqrt(2*math.pi)*s)*math.exp(-0.5*((x-m)/(s))**2)
print g


"""
Output when running program in windows console gaussian1.py

0.282094791774
"""
