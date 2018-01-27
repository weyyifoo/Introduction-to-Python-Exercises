# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:49:45 2018

@author: Wey Yi
"""

# playing around with drawing shapes using the turtle module

import turtle as ttl

ttl.clear()

ttl.pensize(3)
ttl.penup()
ttl.goto(-200,-50)
ttl.pendown()
ttl.circle(20, steps=3)

ttl.pensize(3)
ttl.penup()
ttl.goto(-100,-50)
ttl.pendown()
ttl.circle(20, steps=4)

ttl.pensize(3)
ttl.penup()
ttl.goto(0,-50)
ttl.pendown()
ttl.circle(20, steps=5)

ttl.pensize(3)
ttl.penup()
ttl.goto(100,-50)
ttl.pendown()
ttl.circle(20, steps=6)

ttl.pensize(3)
ttl.penup()
ttl.goto(200,-50)
ttl.pendown()
ttl.circle(20, steps=7)
ttl.penup()
ttl.goto(0,0)