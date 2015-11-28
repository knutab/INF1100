from math import sqrt

"""
since x0 and y0 is not used in the calculations for the area and perimiter of the 
rectangle, and is in no other way needed to get the functions working I am dropping them
in the implementation of the class. 
"""

class Rectangle:
    def __init__(self, W, H):
        self.W, self.H = W, H
        
    def area(self):
        return self.W * self.H
        
    def perimeter(self):
        return self.W * 2 + self.H * 2
        

class Triangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.x0, self.y0, self.x1, self.y1, self.x2, self.y2 = x0, y0, x1, y1, x2, y2
    
    def area(self):
        x0 = self.x0
        y0 = self.y0
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        #Reuses the function from 3.11 to calculate the area of the triangle
        vertices = [(x0, y0), (x1, y1), (x2, y2)]
        v1 = vertices[0]
        v2 = vertices[1]
        v3 = vertices[2]
        area = 0.5*abs(v2[0]*v3[1]-v3[0]*v2[1]-v1[0]*v3[1]+v3[0]*v1[1]+v1[0]*v2[1]-v2[0]*v1[1])
        return area
    
    def perimeter(self):
        x0 = self.x0
        y0 = self.y0
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2

        AB = sqrt((x0 - x1)**2 + (y0 - y1)**2)
        BC = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        AC = sqrt((x0 - x2)**2 + (y0 - y2)**2)
        return AB + BC + AC
        
"""
tests the Rectangle class using W = 2 and H = 2 using same setup as shown in 
test_Circle(): in 7.2
"""
def test_Rectangle():
    W = 2
    H = 2
    r = Rectangle(W, H)
    area = W * H   
    perimiter = W * 2 + H * 2
    diff = abs(r.area() - area)
    tol = 1E-14
    assert diff < tol, 'bug in Rectangle.area, diff=%s' % diff
    diff = abs(r.perimeter() - perimiter)
    assert diff < tol, 'bug in Rectangle.perimiter, diff=%s' % diff

"""
tests the triangle class using the following inputs
v1 = (0, 0) x0 = 0 y0 = 0
v2 = (1, 0) x1 = 1 y1 = 0
v3 = (0, 2) x2 = 0 y2 = 2
"""
def test_Triangle():
    x0 = 0; y0 = 0; x1 = 1; y1 = 0; x2 = 0; y2 = 2
    t = Triangle(x0, y0, x1, y1, x2, y2)
    #Used for the test function and not in the class function
    vertices = [(0,0), (1,0), (0,2)]
    v1 = vertices[0]
    v2 = vertices[1]
    v3 = vertices[2]
    area = 0.5*abs(v2[0]*v3[1]-v3[0]*v2[1]-v1[0]*v3[1]+v3[0]*v1[1]+v1[0]*v2[1]-v2[0]*v1[1])
    AB = sqrt((x0 - x1)**2 + (y0 - y1)**2)
    BC = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    AC = sqrt((x0 - x2)**2 + (y0 - y2)**2)
    perimiter = AB + BC + AC
    diff = abs(t.area() - area)
    tol = 1E-14
    assert diff < tol, 'bug in Rectangle.area, diff=%s' % diff
    diff = abs(t.perimeter() - perimiter)
    assert diff < tol, 'bug in Rectangle.perimiter, diff=%s' % diff
    
    
"""
Running both test functions returns nothing, ie the test i passed
"""