'''
a=[20,10,2,4]
a.sort()
print(a)
#modules
import math
print("The value of pi is", math.pi)
import math as m
print(m.pi)
from math import pi
print("The value of pi is", pi)'''

import modules
print(modules.add(4,5))
import modules as m
print(m.add(45,12))
from modules import add
print(add(78,45))
from modules import*
print(add(45,78))
greeting("Hello")
