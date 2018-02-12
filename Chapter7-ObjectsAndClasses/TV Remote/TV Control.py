# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 08:02:09 2018

@author: Wey Yi
"""

class TV:
    def __init__(self):
        self.channel = channel # default channel is 1
        self.volumelevel = volumelevel # default volume is 1
        self.on = False # initially TV is off
    
    def turnon(self):
        self.on = True
        
    def turnoff(self):
        self.on = False
        
    def getchannel(self):
        