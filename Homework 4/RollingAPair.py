# Homework 5.3                      RollingAPair.py
# Version:                          v1.0.1
# Completed by:                     Anthony Braden on 09/24/2021

# 26.16 LAB: Rolling for a pair
# Given two GVDie objects that represent 2 six-sided dice and an integer that represents a desired value as parameters, complete the function rolling_for_pair(). The function rolling_for_pair() rolls the dice until a pair with the desired value is rolled and then returns the number of rolls thrown to achieve the result. Assume the desired value received from input is within the appropriate range, 1-6.
#
# Note: For testing purposes, the GVDie objects are created in the main() function using a pseudo-random number generator with a fixed seed value. The program uses a seed value of 15 during development, but when submitted, a different seed value will be used for each test case. Refer to the textbook section on random numbers to learn more about pseudo-random numbers.
#
# Ex: If the GVDie objects are created with a seed value of 15 and the input of the program is:
#
# 3
# the output is:
#
# It took 13 rolls to get a pair of 3's.

from GVDie import GVDie

def rolling_for_pair(d1, d2, val):
    d1.roll()
    d2.roll()
    rolls = 1
    while d1.my_value != val or d2.my_value != val:
        d1.roll()
        d2.roll()
        rolls += 1  
    return rolls 

def runAgain():
    startAgain = input("Would you like to roll for another pair? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Bye bye!")
        exit()
    else:
        return runAgain()
    
def runMain():
    die1 = GVDie()   
    die2 = GVDie()   
    die1.set_seed(15)
    die2.set_seed(15)
          
    val = int(input("What integer would you like to roll? > "))
    rolls = rolling_for_pair(die1, die2, val) 
    print(f'It took {rolls} rolls to get a pair of {val}\'s.')
    runAgain()

if __name__ == "__main__":
    runMain()
