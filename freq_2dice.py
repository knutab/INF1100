import random

random.seed(123)

N = 1000000


roll2 = 0
roll3 = 0
roll4 = 0
roll5 = 0
roll6 = 0
roll7 = 0
roll8 = 0
roll9 = 0
roll10 = 0
roll11 = 0
roll12 = 0

for i in xrange(N):
    sum_dice = sum([random.randint(1, 6) for  i in range(2)])
    if sum_dice == 2:
        roll2 += 1
    if sum_dice == 3:
        roll3 += 1
    if sum_dice == 4:
        roll4 += 1
    if sum_dice == 5:
        roll5 +=1
    if sum_dice == 6:
        roll6 += 1
    if sum_dice == 7:
        roll7 += 1
    if sum_dice == 8:
        roll8 += 1
    if sum_dice == 9:
        roll9 += 1
    if sum_dice == 10:
        roll10 += 1
    if sum_dice == 11:
        roll11 += 1
    if sum_dice == 12:
        roll12 += 1
        

prob2 = float(roll2) / N
prob3 = float(roll3) / N
prob4 = float(roll4) / N
prob5 = float(roll5) / N
prob6 = float(roll6) / N
prob7 = float(roll7) / N
prob8 = float(roll8) / N
prob9 = float(roll9) / N
prob10 = float(roll10) / N
prob11 = float(roll11) / N
prob12 = float(roll12) / N

simulated = [prob2, prob3, prob4, prob5, prob6, prob7, prob8, prob9, prob10, prob11, prob12]
number = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
excact = [1./36, 4./72, 6./72, 8./72, 10./72, 12./72, 10./72, 
                8./72, 6./72, 4./72, 1./36]
                

combine = [number, simulated, excact]
print 'Eyes           Simulated     Exact'
for i in range(11):
    print "%.1f            %.5f      %.5f" %(number[i], simulated[i], excact[i])
    
"""
Output when running script with N = 1 000 000 times.
runfile('C:/Users/1234/OneDrive/UiO INF1100/innlevering 10/freq_2dice.py', wdir='C:/Users/1234/OneDrive/UiO INF1100/innlevering 10')
Eyes           Simulated     Exact
2.0            0.02777      0.02778
3.0            0.05570      0.05556
4.0            0.08344      0.08333
5.0            0.11054      0.11111
6.0            0.13879      0.13889
7.0            0.16663      0.16667
8.0            0.13959      0.13889
9.0            0.11061      0.11111
10.0            0.08348      0.08333
11.0            0.05538      0.05556
12.0            0.02807      0.02778
"""