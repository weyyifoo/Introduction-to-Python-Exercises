# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:15:29 2018

@author: Wey Yi
"""

class Rocket():
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def moveup():
        self.y += 1
    
    def movedown():
        self.y -= 1
        
    def moveright():
        self.x += 1
        
    def moveleft():
        self.x -= 1
        
myrocket = Rocket()
print("Your rocket's current position is ", myrocket.x, " ", myrocket.y)

while True:
    next = eval(input("What is your rocket's next step? \n"
                      "1. Move Up \n"
                      "2. Move Down \n"
                      "3. Move Right \n"
                      "4. Move Left \n"
                      "5. Print Rocket's current position \n"
                      "6. Explode \n"
                      "Enter step: "
                      ))
    if next == 1:
        myrocket.moveup()
    if next == 2:
        myrocket.movedown()
        if myrocket.y < 0:
            print("Rocket has crashed")
    if next == 3:
        myrocket.moveright()
    if next == 4:
        myrocket.moveleft()
    if next == 5:
        print(myrocket.x, " ", myrocket.y)
    if next == 6:
        quit()