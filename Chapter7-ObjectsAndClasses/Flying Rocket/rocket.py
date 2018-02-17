# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:05:52 2018

@author: Wey Yi
"""

class Rocket():
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def moveup(self):
        self.y += 1
        
myrocket = Rocket()
print(myrocket)

myrocket.moveup()
print("Rocket's current altitude", myrocket.y)

myrocket.moveup()
print("Rocket's current altitude", myrocket.y)

myrocket.moveup()
print("Rocket's current altitude", myrocket.y)