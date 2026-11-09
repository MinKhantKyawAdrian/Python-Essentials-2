#Import the module
import math
print(math.sin(math.pi/2))

from math import sin, pi
print(sin(pi/2))

#Not import the module so need to define 
pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

#Aliasing
import math as m    
print(m.sin(m.pi/2))