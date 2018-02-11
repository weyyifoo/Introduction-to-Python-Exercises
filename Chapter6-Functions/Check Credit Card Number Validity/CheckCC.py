# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 12:31:25 2018

@author: Wey Yi
"""

# module for the first step where each integer is multipled by 2. if the result is greater than 10,
# each integer is added together
def multi2(u):
    if len(str(u)) == 16:
        for n in range(16):
            ele = (u % 10)*2 #multiplies the remainder of cc/10 by 2
            u //= 10 #takes cc and does a floor division
            if ele > 9: # if the result is more than 9
                b = (ele % 10) # divides ele by 10, records b
                ele //= 10 # divides ele by 10 and records floor
                d = b + ele
                cc2.append(d)
            else:
                cc2.append(ele)
    else:
        print('You need to enter 16 digits')
    return cc2

# step 2, where each digit is added up
def sumup(s):
    cc3 = sum(s)
    return cc3

cc = int(input('Please enter Credit Card Number: '))
cc2 = []
multi2(cc)
sumup(cc2)