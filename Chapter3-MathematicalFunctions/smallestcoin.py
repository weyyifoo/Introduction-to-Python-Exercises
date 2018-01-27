# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:12:51 2018

@author: Wey Yi
"""

## 3.4 Case Study: Minimum Number of Coins.
#Now let’s look at a sample program that uses the features covered in this section. Suppose you
#want to develop a program that classifies a given amount of money into smaller monetary
#units. The program lets the user enter an amount as a floating-point value representing a total
#in dollars and cents, and then outputs a report listing the monetary equivalent in dollars, quarters, dimes, nickels, and pennies, as shown in the sample run.
#Your program should report the maximum number of dollars, then the number of quarters,
#dimes, nickels, and pennies, in this order, to result in the minimum number of coins

import math

print('This script calculates for the smallest number of coins you can have')
amount = float(input('How many dollars would you like to calculate this for? '))
amountincents = amount*100

# Number of dollars
DollarNumber = amountincents/100
NumDollars = math.floor(DollarNumber)
print('There are ',NumDollars,"\b dollar bills in the amount calculated")

# Number of quarters
RemainderAmount = amountincents%100
NumQuarters = math.floor(RemainderAmount/25)
print('There are ',NumQuarters,"\b quarters in the amount calculated")

# Number of dimes
RemainderAmount2 = RemainderAmount%25
NumDimes = math.floor(RemainderAmount2/10)
print('There are ',NumDimes,"\b dimes in the amount calculated")

# Number of nickels
RemainderAmount3 = RemainderAmount2%10
NumNickels = math.floor(RemainderAmount3/1)
print('There are ',NumNickels,"\b nickels in the amount calculated")

Sum = NumDollars + NumQuarters + NumDimes + NumNickels

print('The smallest number of coins you can have from the amount entered is',Sum )