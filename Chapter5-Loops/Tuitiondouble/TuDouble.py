# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:04:51 2018

@author: Wey Yi
"""

# how long will tuition take to double?

init = eval(input('how much was tuition initially?: '))
tuition = init
year = 0

while (tuition/init) <= 2:
    tuition = tuition*1.07
    year += 1
    
print('it will take ', year, 'years before tuition doubles from its current rate of ', init)