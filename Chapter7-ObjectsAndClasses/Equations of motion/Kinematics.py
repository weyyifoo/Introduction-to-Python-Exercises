# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:36:32 2018

@author: Wey Yi
"""

# solving kinematic equations

import math

class Rocket():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vi = 0
        self.vix = 0
        self.viy = 0
        self.t = 0
        self.a = 0
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
print(myrocket.vix)
print(myrocket.viy)

