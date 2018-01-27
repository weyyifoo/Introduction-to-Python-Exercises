# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:48:02 2018

@author: Wey Yi
"""

status = eval(input(
        "(0-single filer, 1-married jointly, \n" +
        "2-married separately, 3-head of household)\n" +
        "Enter filing status: "))
        
Tincome = eval(input("Enter your taxable income: $"))

# compute tax
Tax = 0

if status == 0: # Compute tax for single filers
    if Tincome <= 8350:
        tax = Tincome * 0.10
    elif Tincome <= 33950:
        tax = 8350 * 0.10 + (Tincome - 8350) * 0.15
    elif Tincome <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (Tincome - 33950) * 0.25
    elif Tincome <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (82250 - 33950) * 0.25 + (Tincome - 82250) * 0.28
    elif Tincome <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
        (Tincome - 171550) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
        (372950 - 171550) * 0.33 + (Tincome - 372950) * 0.35;
elif status == 1:
    print("Left out of exercise")
elif status == 2:
    print("Left out of exercise")
elif status == 3:
    print("Left out of exercise")
    
print("Tax is $", tax)