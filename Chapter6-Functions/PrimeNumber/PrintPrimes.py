# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

def PrPrimeNo(numberofprimes):
    NoPr = 50
    NoPrPL = 10
    count = 0
    number = 2
    
    while count < NoPr:
        if isPrime(number):
            count += 1
            print(number, end = ' ')
            if count % NoPrPL == 0:
                print()
                
        number += 1
        
def main():
    print("The first 50 prime numbers are")
    PrPrimeNo(50)
    
main()