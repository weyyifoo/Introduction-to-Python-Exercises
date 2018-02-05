# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:19:17 2018

@author: Wey Yi
"""

def GetGrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def printGrade():
    score = eval(input('enter student\'s score: '))
    print(GetGrade(score))

printGrade()