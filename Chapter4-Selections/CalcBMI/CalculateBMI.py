# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:48:04 2018

@author: Wey Yi
"""

# prompt user to enter weight:
weight = eval(input('Please enter your weight in pounds: '))

# prompt user to enter height
height = eval(input('Please enter your height in inches: '))

kg_lbs = 0.45359237
m_inch = 0.0254

# computer BMI
weightinKG = weight * kg_lbs
heightinM = height * m_inch
bmi = weightinKG / (heightinM**2)

# display result
print("BMI is ", format(bmi,"0.2f"))
if bmi < 18.5:
    print("you are underweight")
elif bmi < 25:
    print("you are normal weight")
elif bmi < 30:
    print("you are overweight")
else:
    print("you are obese")
    
print('at your height, you normal weight will have to be between', format(((20*(heightinM**2))/kg_lbs),"0.1f"), 'and', format(((25*(heightinM**2))/kg_lbs),"0.1f"))