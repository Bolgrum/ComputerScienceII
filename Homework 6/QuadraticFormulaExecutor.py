# Homework 6.3                      QuadraticFormula.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 10/08/2021

# Implement the quadratic_formula() function. The function takes 
# 3 arguments, a, b, and c, and computes the two results of the 
# quadratic formula:
#
# The quadratic_formula() function returns the tuple (x1, x2). 
# Ex: When a = 1, b = -5, and c = 6, quadratic_formula() returns 
# (3, 2).
#
# Code provided in main.py reads a single input line containing 
# values for a, b, and c, separated by spaces. Each input is 
# converted to a float and passed to the quadratic_formula() 
# function.
#
# Ex: If the input is:
#
# 2 -3 -77
# the output is:
#
# Solutions to 2x^2 + -3x + -77 = 0
# x1 = 7
# x2 = -5.50

import math
import QuadraticFormula

def printNumber(number, prefixString):
    if float(int(number)) == number:
        print(f'{prefixString}{number:.0f}')
    else:
        print(f'{prefixString}{number:.2f}')


if __name__ == "__main__":
    inputLine = input("Please enter your three coefficients with a space between them:\n(x1 x2 x3)> ")
    splitLine = inputLine.split(" ")
    a = float(splitLine[0])
    b = float(splitLine[1])
    c = float(splitLine[2])
    solution = QuadraticFormula.quadraticFormula(a, b, c)

    print(f'Solutions to {a:.0f}x^2 + {b:.0f}x + {c:.0f} = 0')
    printNumber(solution[0], 'x1 = ')
    printNumber(solution[1], 'x2 = ')
