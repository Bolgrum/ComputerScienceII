# Homework 6.2                      GuessRandomNumber.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 10/08/2021

# 11.9 LAB: Guess the random number
# Given the code that reads a list of integers, complete the 
# number_guess() function, which should choose a random number 
# between 1 and 100 by calling random.randint() and then output 
# if the guessed number is too low, too high, or correct.
#
# Import the random module to use the random.seed() and 
# random.randint() functions.
#
# random.seed(seed_value) seeds the random number generator 
# using the given seed_value.
# random.randint(a, b) returns a random number between a and b 
# (inclusive).
# For testing purposes, use the seed value 900, which will cause 
# the computer to choose the same random number every time the 
# program runs.
#
# Ex: If the input is:
#
# 32 45 48 80
# the output is:
#
# 32 is too low. Random number was 80.
# 45 is too high. Random number was 30.
# 48 is correct!
# 80 is too low. Random number was 97.

import random

def findNum(a, b):
    left = a    
    right = b
    guess = (a + b) // 2 
    return guess

def numberGuess(a, b):
    randomNumber = random.randint(a, b)
    print("\nThe random number is", randomNumber)
    return randomNumber

def runAgain():
    startAgain = input("Would you like to perform another guess? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Exiting program.")
        exit()
    else:
        return runAgain()

def runMain():
    count = 0
    guess = 0
    a = 1
    b = 100
    random.seed()
    randomNumber = numberGuess(a, b)
    while (guess != randomNumber):
        count += 1
        guess = findNum(a, b)
        if guess < randomNumber:
            print(f"\nThe computer guessed {guess}.\nThat number was too low.")
            a = guess + 1
        elif guess > randomNumber:
            print(f"\nThe computer guessed {guess}.\nThat number was too high.")
            b = guess - 1
    if count == 1:
        print(f"\nThe program guessed {randomNumber} in {count} guess.")
    else:
        print(f"\nThe program guessed {randomNumber} in {count} guesses.")  
    runAgain()  
        
if __name__ == "__main__":
    runMain()