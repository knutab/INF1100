import csv

x0 = 100
p = 5
N = 4

x_nminus1 = x0
n = 0
results =[]

while n < N:
    x_n = x_nminus1 + (p/100.0)*x_nminus1
    results.append(x_n)  
    x_nminus1 = x_n
    n += 1

#Writes result to csv file named test
with open('test.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in results:
        writer.writerow([val])
    
"""
No running example, csv file of output saved in same folder as script.
"""