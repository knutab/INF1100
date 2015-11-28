import math

    
C_d=0.2
e=1.2                  #kg/m^3
m=0.43                 #kg
g=9.81                 #m/s^2
a=0.11                 #m
A=math.pi * a**2       #m

V_hard=33.3333333      #m/s
V_soft=2.77777778      #m/s

#Calculates the drag force for the soft kick
F_d_soft = 0.5 * C_d * e * A * V_soft**2

#Calculates the drag force for the hard kick
F_d_hard = 0.5 * C_d * e * A * V_hard**2

#Calculates the gravity force vorking on the ball
F_g = m * g

Ratio_soft_drag = F_d_soft / F_g
Ratio_soft_gravity = F_g / F_d_soft

Ratio_hard_drag = F_d_hard / F_g
Ratio_hard_gravity = F_g / F_d_hard 

print 'Soft kick: drag is %.1f, drag ratio is %.1f, gravity pull is %.1f, gravity ratio is %.1f' %(F_d_soft, Ratio_soft_drag, F_g, Ratio_soft_gravity)
print 'Hard kick: drag is %.1f, drag ratio is %.1f, gravity pull is %.1f, gravity ratio is %.1f' %(F_d_hard, Ratio_hard_drag, F_g, Ratio_hard_gravity)                                                                                     
        

"""
Output when running program in windows console kick.py

Soft kick: drag is 0.0, drag ratio is 0.0, gravity pull is 4.2, gravity ratio is 1.0
Hard kick: drag is 5.1, drag ratio is 0.5, gravity pull is 4.2, gravity ratio is 0.5
"""
