# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:09:06 2018

@author: Wey Yi
"""

def max(i,j):
    if i > j:
        k = i
    else:
        k = j  
    return k

def main():
    i = 203
    j = 502
    k = max(i,j)
    
    print('the max of ', i, ' and ', j, ' is ', k)

main()