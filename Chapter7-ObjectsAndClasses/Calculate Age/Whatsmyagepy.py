# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:40:44 2018

@author: Wey Yi
"""

import datetime

class Person:
    def __init__(self, firstname, lastname, birthdate, address, telephone, email, profession):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.profession = profession
        
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
    
    def fullname(self):
        return self.firstname + " " + self.lastname
    
person1 = Person(
        "Sansa",
        "Stark",
        datetime.date(1990, 12, 25),
        "Winterfell",
        "Crow-305",
        "SansaStark@HouseStark.com",
        "Lady Stark")

person2 = Person("Ned",
                 "Stark",
                 datetime.date(1960, 1, 1),
                 "Winterfell",
                 "Raven-1",
                 "NedStark@HouseStark.com",
                 "He ded")

print(person1.fullname(), "\'s age is", person1.age())
print(person2.fullname(), "\'s age is", person2.age())