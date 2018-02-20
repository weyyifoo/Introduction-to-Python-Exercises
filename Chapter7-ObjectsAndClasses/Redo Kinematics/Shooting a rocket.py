# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:28:02 2018

@author: Wey Yi
"""

import math

class Rocket():
    def __init__(self, vi, theta):
        self.vi = vi
        self.vx = self
        self.vy = self
        self.theta = math.radians(theta)
        self.t = self
        self.g = -10
        self.x = self
        self.y = self
        self.d = self

    def resolvexy(self):
        self.vx = self.vi * math.cos(self.theta)
        self.vy = self.vi * math.sin(self.theta)
        
    def solvet(self):
        self.t = 2*(0 - self.vy)/(self.g)
        return self.t
    
    def distancexy(self):
        self.x = self.vx * self.t
        self.y = self.g * ((self.t)**2)
        self.d = self.vx * self.t
        return self.x
        return self.y
        
rocket1 = Rocket(eval(input("Enter initial velocty: ")), eval(input("Enter angle of firing: ")))
rocket1.resolvexy()
rocket1.solvet()
rocket1.distancexy()

print("%.2f" % rocket1.t)
print("vx is", "%.2f" % rocket1.vx)
print("vy is", "%.2f" % rocket1.vy)