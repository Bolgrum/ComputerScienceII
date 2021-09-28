# Homework 5.2                      HowManyDiceRolls.py
# Version:                          v1.0.1
# Completed by:                     Anthony Braden on 09/24/2021

# 26.7 LAB: How many dice rolls?
# Given a GVDie object and an integer that represents the total 
# sum desired as parameters, complete function roll_total() that 
# returns the number of rolls needed to achieve at least the total 
# sum.
#
# Note: For testing purposes, the GVDie object is created in the 
# main() function using a pseudo-random number generator with a 
# fixed seed value. The program uses a seed value of 15 during 
# development, but when submitted, a different seed value will be 
# used for each test case. Refer to the textbook section on 
# random numbers to learn more about pseudo-random numbers.
#
# Ex: If the GVDie object is created with a seed value of 15 and 
# the input of the program is:
#
# 20
# the output is:
#
# Number of rolls to reach at least 20: 8

from GVDie import GVDie
import random

def roll_total(die, total):
    total_value = 0
    total_rolls = 0
    while total_value < total:
        die.roll()
        total_value += die.my_value
        total_rolls += 1
    return total_rolls 
    
if __name__ == "__main__":
    die = GVDie()   
    die.set_seed(15)   
          
    total = int(input())
    rolls = roll_total(die, total) 
    print(f'Number of rolls to reach at least {total}: {rolls}')