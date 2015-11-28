


def area(vertices):
    """
    Calculates the areal of a triangle by taking the vertex cordinates as an 
    input. Input needs to be entered as a nested list where v1 here points to the first 
    vertex, and v1[0] will select the x value, and v1[1] will select the y value.    
    """
    v1 = vertices[0]
    v2 = vertices[1]
    v3 = vertices[2]
    Area = 0.5*abs(v2[0]*v3[1]-v3[0]*v2[1]-v1[0]*v3[1]+v3[0]*v1[1]+v1[0]*v2[1]-v2[0]*v1[1])
    return Area
    
v1 = (0, 0)
v2 = (1, 0)
v3 = (0, 2)

vertices = [v1, v2, v3]

triangle1 = area(vertices)

print 'Area of triangle is %.2f' % triangle1


"""
Output when running program in windows console area_triangle.py

Area of triangle is 1.00
"""