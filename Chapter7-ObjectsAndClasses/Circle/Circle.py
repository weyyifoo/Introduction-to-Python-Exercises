# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 18:57:28 2018

@author: Wey Yi
"""

import math

class Circle:
    # Construct a circle object
    def __init__(self, radius = 1):
        self.radius = radius
    
    def getPerimeter(self):
        return 2 * self.radius * math.pi
    
    def getArea(self):
        return self.radius * self.radius * math.pi
    
    def setRadius(self, radius):
        self.radius = radius
        
from Circle import Circle

c = Circle(5)
c.radius

print("Area is", Circle(3).getArea())