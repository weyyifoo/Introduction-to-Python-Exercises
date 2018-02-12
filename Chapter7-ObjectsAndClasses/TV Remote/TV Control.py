# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 08:02:09 2018

@author: Wey Yi
"""

class TV:
    def __init__(self):
        self.channel = 1 # default channel is 1
        self.volumelevel = 1 # default volume is 1
        self.on = False # initially TV is off
    
    def turnon(self):
        self.on = True
        
    def turnoff(self):
        self.on = False
        
    def getchannel(self):
        return self.channel
    
    def setchannel(self, channel):
        if (self.on is True) and (1 <= self.channel <= 200):
            self.channel = channel
            
    def setvolume(self, volumelevel):
        if (self.on is True) and (1 <= self.volumelevel <= 100):
            self.volumelevel = volumelevel
            
    def channelup(self):
        if (self.on is True) and (self.channel < 120):
            self.channel += 1
            
    def channeldown(self):
        if (self.on is True) and (self.channel > 1):
            self.channel -= 1
    
    def volumeup(self):
        if (self.volumelevel) < 100:
            self.volumelevel += 1
    
    def volumedown(self):
        if (self.volumelevel) > 1:
            self.volumelevel -= 1
            
def main():
    tv1 = TV()
    tv1.turnon()
    tv1.setchannel(50)
    tv1.setvolume(20)
    print(tv1.getchannel())
    
main()