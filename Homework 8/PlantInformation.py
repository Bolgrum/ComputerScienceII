# Homework 8.2                      PookInformation.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 10/29/2021

# 13.11 LAB: Plant information
# Given a base Plant class and a derived Flower class, write a 
# program to create a list called myGarden. Store objects that 
# belong to the Plant class or the Flower class in the list. 
# Create a function called printList(), that uses the 
# printInfo() instance methods defined in the respective 
# classes and prints each element in myGarden. The program 
# should read plants or flowers from input (ending with -1), add 
# each Plant or Flower to the myGarden list, and output each 
# element in myGarden using the printInfo() function.
#
# Note: A list can contain different data type and also different objects.
#
# Ex. If the input is:

# plant Spirea 10
# flower Hydrangea 30 false lilac
# flower Rose 6 false white
# plant Mint 4
# -1
# the output is:
# 
# Plant Information:
# Plant name: Spirea
# Cost: 10
# 
# Plant Information:
# Plant name: Hydrangea
# Cost: 30
# Annual: false
# Color of flowers: lilac
# 
# Plant Information:
# Plant name: Rose
# Cost: 6
# Annual: false
# Color of flowers: white
# 
# Plant Information:
# Plant name: Mint
# Cost: 4

class Plant:
    def __init__(self, plantName, plantCost):
        self.plantName = plantName
        self.plantCost = plantCost

    def printInfo(self):
        print('Plant Information:')
        print('   Plant name:',self.plantName)
        print('   Cost: $' + self.plantCost)

class Flower(Plant):
    def __init__(self, plantName, plantCost, isAnnual, colorOfFlowers):
        Plant.__init__(self, plantName, plantCost)
        self.isAnnual = isAnnual
        self.colorOfFlowers = colorOfFlowers

    def printInfo(self):
        print('Plant Information:')
        print('   Plant name:',self.plantName)
        print('   Cost: $' + self.plantCost)
        print('   Annual:',self.isAnnual)
        print('   Color of flowers:',self.colorOfFlowers)

def printList(myGarden):
    for i in range(len(myGarden)):
        myGarden[i].printInfo()
        print()

if __name__ == "__main__":
    myGarden = []
    userInput = input()
    while userInput != '-1':
        tokens = userInput.split()
        if tokens[0] == 'plant':
            name = tokens[1]
            cost = tokens[2]
            myPlant = Plant(name, cost)
            myGarden.append(myPlant)
        elif tokens[0] == 'flower':
            name = tokens[1]
            cost = tokens[2]
            type = tokens[3]
            color = tokens[4]
            myFlower = Flower(name, cost, type, color)
            myGarden.append(myFlower)
        userInput = input()

    printList(myGarden)