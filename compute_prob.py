import random

def compute_prob(N):
    M = 0
    for i in xrange(N):
        outcome = random.random()
        if 0.5 < outcome < 0.6:
            M += 1
            
    return float(M)/N
    

N_1 = 10**1
N_2 = 10**2
N_3 = 10**3
N_6 = 10**6

print 'Probability that value is between 0.5 and 0.6 is %.3f when N is %s.' %(compute_prob(N_1), N_1)
print 'Probability that value is between 0.5 and 0.6 is %.3f when N is %s.' %(compute_prob(N_2), N_2)
print 'Probability that value is between 0.5 and 0.6 is %.3f when N is %s.' %(compute_prob(N_3), N_3)
print 'Probability that value is between 0.5 and 0.6 is %.3f when N is %s.' %(compute_prob(N_6), N_6)

"""
Running Example running file in Spyder
runfile('C:/Users/1234/OneDrive/UiO INF1100/innlevering 10/compute_prob.py', wdir='C:/Users/1234/OneDrive/UiO INF1100/innlevering 10')
Probability that value is between 0.5 and 0.6 is 0.100 when N is 10.
Probability that value is between 0.5 and 0.6 is 0.110 when N is 100.
Probability that value is between 0.5 and 0.6 is 0.104 when N is 1000.
Probability that value is between 0.5 and 0.6 is 0.100 when N is 1000000.
"""