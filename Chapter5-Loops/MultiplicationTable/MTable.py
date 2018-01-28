# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:00:47 2018

@author: Wey Yi
"""

# Multiplication table

print('                   Multiplication table')

# Display the number title
print('  |', end = ' ')
for j in range(1,10):
    print(' ', j, end = '  ')
print()
print('-------------------------------------------')

# Display table body
for i in range(1,10): # prints 1st column listing multiple
    print(i, '|', end = '') 
    for j in range(1,10): # prints the result
        print(format(i*j, "4d"), end = ' ')
    print() # goes to next column and loops back