# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:36:32 2018

@author: Wey Yi
"""

# solving kinematic equation for a rocket pointing at an angle

import math

class Rocket():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vi = 0
        self.vix = 0
        self.viy = 0
        self.t = 0
        self.ttop = 0
        self.tbottom = 0
        self.g = 9.81
        self.angle = 0
        
    def setangle(self):
        self.angle = math.radians(eval(input("at what angle from the horizontal is the cannon pointed at?: ")))
        
    def setvi(self):
        self.vi = eval(input("Enter the initial speed of the project in m/s: "))
        
    def setvxvy(self):
        self.vix = math.cos(myrocket.angle)*myrocket.vi
        self.viy = math.sin(myrocket.angle)*myrocket.vi
        
    def setx(self):
        self.x += 1
        
    def time(self):
        self.ttop = (myrocket.vi)/(myrocket.g)
        self.tbottom = (2*myrocket.viy)/(myrocket.g)
        self.t = self.ttop + self.tbottom
        
myrocket = Rocket()

# set angle of rocket
myrocket.setangle()
print("The angle of the cannon is now set to", math.degrees(myrocket.angle), "degrees from the horizontal")
# set initial velocity of rocket
myrocket.setvi()

while True:
    if myrocket.vi <= 0:
        print("Error: projectile\'s initial velocity cannot be less than or equal to 0")
        myrocket.setvi()
    else:
        break

# calculate vix and viy
myrocket.setvxvy()
print("X-velocity:", "%.2f" % myrocket.vix)
print("Y-velocity:", "%.2f" % myrocket.viy)

myrocket.time()
print("Rocket flight time:", "%.2f" % myrocket.t)