

#a)

def H(x):
    
    if x < 0:
        return 0
    else:
        return 1
#b)

"""
Tests the first value of x = -10 with a test function as described in the 
video lecture 9. september, oppgave 2.19, 2.20, 3.2 H14. And tests the rest
of the values just by running the function for those values.
"""

# Rules for test function:
# 1. name: test_*
# 2. no arguments
# 3. introduce boolean variable success:
# True if test is passed, otherwise False
# 4. end with assert success

def test_H():
    exact = 0
    computed = H(-10)
    assert computed == exact
    
    
test_H()
    
print 'Test for x=-10^-15 should return 0, and it returns %d' % H(-10**-15) 
print 'Test for x=0 should return 1, and it returns %d' % H(0) 
print 'Test for x=10^-15 should return 1, and it returns %d' % H(10**-15) 
print 'Test for x=10 should return 1, and it returns %d' % H(10) 


"""
Output when running program in windows console Heaviside.py

Test for x=-10^-15 should return 0, and it returns 0
Test for x=0 should return 1, and it returns 1
Test for x=10^-15 should return 1, and it returns 1
Test for x=10 should return 1, and it returns 1
"""