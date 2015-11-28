import math

def gauss(x, m=0, s=1):
    fx = 1./(math.sqrt(2*math.pi)*s)*math.exp(-0.5*(float(x-m)/s)**2)
    return fx
 
   
"""
Chooses to create the table for the interval x=-5 to x=5 where x is 
increased by one for each itteration.
"""
list1 = []          #list created to hold the x values
list2 = []          #list created to hold the f(x) values

x = -5              #Starting value of x
dF = 1              #increment of x

while x <=5:
    f_x = gauss(x)
    list1.append(x)
    list2.append(f_x)
    x = x + dF
  
#Uses same method to print the list as for f2c_approx_table.py  
table =[]                             
for e1, e2 in zip(list1, list2):
    table.append([e1, e2])
    

print '----x-------f(x)------'
print ' '

for e1, e2 in table:
    print '%5d    %5.10f' %(e1, e2)
    

"""
Output when running program in windows console gaussian2.py

----x-------f(x)------
 
   -5    0.0000014867
   -4    0.0001338302
   -3    0.0044318484
   -2    0.0539909665
   -1    0.2419707245
    0    0.3989422804
    1    0.2419707245
    2    0.0539909665
    3    0.0044318484
    4    0.0001338302
    5    0.0000014867
"""
