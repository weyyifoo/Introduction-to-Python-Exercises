# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:28:02 2018

@author: Wey Yi
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

class Rocket():
    def __init__(self, vi, theta):
        self.vi = vi
        self.vx = self
        self.vy = self
        self.theta = math.radians(theta)
        self.t = self
        self.g = -9.81
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


# panel setup for where the function will be plotted unto
fig1 = plt.figure()
ax = plt.axes(xlim = (0, rocket1.d), ylim = (0, rocket1.y))
line, = ax.plot([], [], lw = 2)

# initialization function: plotting the background of each frame
def init():
    line.set_data([], [])
    t1 = np.arange(0, rocket1.t, 0.1)
    return line,

# define function and animate
def animate(i):
    x1 = rocket1.vx * t1[i]
    y1 = rocket1.vy * t1[i] - 0.5 * rocket1.g * (t[i])**2
    line.set_data(x1, y1)
    return line,

# call the animation.
anim = animation.FuncAnimation(fig1, animate, init_func = init, 
                               frames = 200, interval = 200,
                               blit = True)
plt.show()