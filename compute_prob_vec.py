import numpy as np

def compute_prob(N):
    r = np.random.uniform(size = N)
    r1 = r[r>0.5]
    r1 = r1[r1<0.6]
    prob = len(r1) / float(N)
    
    return prob

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
runfile('C:/Users/1234/OneDrive/UiO INF1100/innlevering 10/compute_prob_vec.py', wdir='C:/Users/1234/OneDrive/UiO INF1100/innlevering 10')
Probability that value is between 0.5 and 0.6 is 0.200 when N is 10.
Probability that value is between 0.5 and 0.6 is 0.130 when N is 100.
Probability that value is between 0.5 and 0.6 is 0.105 when N is 1000.
Probability that value is between 0.5 and 0.6 is 0.100 when N is 1000000.
"""