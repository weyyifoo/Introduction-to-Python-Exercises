# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 16:43:16 2018

@author: Wey Yi
"""

import turtle as ttl
import random

ttl.clear()

# define coord for center of circle
x1, y1 = (0, 0)
print("the center of the circle lies at 0, 0")
radius = eval(input("Enter the radius of the circle between 0 to 100: "))
x2, y2 = ((random.random()*100), (random.random()*100))

#drawing the circle
ttl.penup()
ttl.goto(x1, y1 - radius)
ttl.pendown()
ttl.circle(radius)

ttl.penup()
ttl.goto(x2, y2)
ttl.pendown()
ttl.begin_fill()
ttl.color("red")
ttl.circle(3)
ttl.end_fill()

d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

ttl.penup()
ttl.goto(x1 - 70, y1 - radius - 20)
ttl.pendown()
if d <= radius:
    ttl.write("the point is inside the circle")
else:
    ttl.write("the point is outside the circle")
    
ttl.hideturtle()
ttl.done()