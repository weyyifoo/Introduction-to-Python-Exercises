# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 11:46:48 2018

@author: Wey Yi
"""

n1 = eval(input('record your first input: '))
n2 = eval(input('record your second input: '))

gcd = 1 #starting gcd integer
k = 2

while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1

# print result out
print('the greatest common denominator between ',
      n1, ' and ', n2, 
      ' is ', gcd)