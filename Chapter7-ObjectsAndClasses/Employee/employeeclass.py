# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:19:13 2018

@author: Wey Yi
"""

# employee class

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('Davis', 'Brown', 50000)
emp_2 = Employee('Lisa', 'Kudrow', 60000)

print(emp_1.last)
print(emp_2.email)
print(emp_1.fname())

print(emp_1.fname())
print(Employee.fname(emp_1))