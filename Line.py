
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def value(self, x):
        p1 = self.p1
        p2 = self.p2
        
        a = (p2[1] - p1[1]) / float( p2[0] - p1[0])
        b = p1[1] - a * p1[0]
        
        return a * x + b
 
       
#From the code example in 7.6 we know that line.value(0.5) for cordinates p1=(0, -1)
# and p2=(2, 4) is 0.25 so we can use that value in the test function        
def test_Line():
    p1 = (0, -1)
    p2 = (2, 4)
    l = Line(p1, p2)
        
    value = 0.25
    diff = abs(l.value(0.5) - value)
    tol = 1E-14
    assert diff < tol, 'Bug in Line.value, diff =%s' % diff