# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:45:34 2018

@author: Wey Yi
"""

def GCD(x1,x2):
    gcd = 1
    n = 1
    
    while (x1 >= n) and (x2 >= n):
        if (x1 % n == 0) and (x2 % n == 0):
            gcd = n
            n += 1
        else:
            n += 1
    return gcd

print(GCD(12,24))