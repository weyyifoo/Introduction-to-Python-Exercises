# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:54:00 2018

@author: Wey Yi
"""

#Print the Calendar for a month in a year
def printMth(year, month):
    #Print calendar headings
    printMthTitle(year, month)
    #Print calendar body
    printMthBody(year, month)
    
def printMthTitle(year, month):
    print("              ", getMthName(month), " ", year)
    print("——————————————————————————————————————————")
    print(" Sun Mon Tue Wed Thu Fri Sat")
    
#Print calendar body
def printMthBody(year, month):
    #Get start day
    startday = getStartDay(year, month)
    #Get number of days in month
    numberofdays = getNumberOfDays(year, month)
    
    #pad space
    i = 0
    for i in range(0, startday):
        print("    ", end = " ")
        
    for i in range(1, numberofdays + 1):
        print(format(i, "4d"), end = " ")
        
        if (i + startday) % 7 == 0:
            print()

# Get the English name for the month
def getMthName(month):
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8:
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    else:
        monthName = "December"
    
    return monthName

# Get startday
def getStartDay(year, month):
    Jan11800 = 3
    
    totalNoDays = getTotalDays(year, month)
    
    return (totalNoDays + Jan11800) % 7

# Get the total number of days since January 1, 1800
def getTotalDays(year, month):
    total = 0
# Get the total days from 1800 to 1/1/year
    for i in range(1800, year):
        if isLeapYear(i):
            total = total + 366
        else:
            total = total + 365

# Add days from Jan to the month prior to the calendar month
    for i in range(1, month):
        total = total + getNumberOfDays(year, i)

    return total

def getNumberOfDays(year, month):
# Get the number of days in a month
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        return 29 if isLeapYear(year) else 28
    return 0 # If month is incorrect

# Determine if it is a leap year
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
# Prompt the user for year and month
    year = eval(input("Enter full year (e.g., 2001): "))
    month = eval(input(("Enter month as number between 1 and 12: ")))

# Print calendar for the month of the year
    printMth(year, month)

main() # Call the main function