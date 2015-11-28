



#Creates empty lists to hold the results
f = []                 
c_app = []
c =[]


F = 0                             #starting value of F                       
dF = 10                           #increment of F 


while F <= 100:                 
    C = F/(9.0/5) - 32.0          #Formula for converting F to C
    C_app = (F - 30.0)/2.0        #Formula for approximation of C
    f.append(F)
    c.append(C)
    c_app.append(C_app)

    F = F + dF


#Creates a table and appends list into it to get a nice
#format on the print
table =[]                             
for e1, e2, e3 in zip(f, c, c_app):
    table.append([e1, e2, e3])


print '----F-------C-------Capp---'
print ' '

for e1, e2, e3 in table:
    print '%5d    %5.1f    %5.1f' %(e1, e2, e3)


"""
Output when running program in windows console f2c_approx_table.py

----F-------C-------Capp---
 
    0    -32.0    -15.0
   10    -26.4    -10.0
   20    -20.9     -5.0
   30    -15.3      0.0
   40     -9.8      5.0
   50     -4.2     10.0
   60      1.3     15.0
   70      6.9     20.0
   80     12.4     25.0
   90     18.0     30.0
  100     23.6     35.0
"""
