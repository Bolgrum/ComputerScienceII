# Homework 4.1                      VendingMachine.py
# Version:                          v1.0.1
# Completed by:                     Anthony Braden on 09/24/2021

# 9.16 LAB: Vending Machine
# Given two integers as user inputs that represent the number of 
# drinks to buy and the number of bottles to restock, create a 
# VendingMachine object that performs the following operations:
# 
# Purchases input number of drinks
# Restocks input number of bottles
# Reports inventory
# A VendingMachine's initial inventory is 20 drinks.
#
# Ex: If the input is:
#
# 5
# 2
# the output is:
#
# Inventory: 17 bottles

class VendingMachine:
    def __init__(self):
        file = open('inventory.txt', 'r')
        contents = file.read()
        self.bottles = int(contents)
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def getInventory(self):
        return self.bottles
        
    def report(self):
        with open('inventory.txt', 'w') as f:
            f.write(str(self.bottles))
        print(f'Inventory: {self.bottles} bottles')

def runAgain():
    startAgain = input("Would you like to check stock or generate another report? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Exiting program.")
        exit()
    else:
        return runAgain()

def runMain():
    drinkMachine = VendingMachine()
    userChoice = input('Would you like to (A) check stock or (B) generate report? (A/B) > ')
    if userChoice.lower() == 'a':
        bottles = drinkMachine.getInventory()
        print(bottles)
    elif userChoice.lower() == 'b':
        drinksToBuy = int(input('How many drinks have been bought? > '))
        bottlesToStock = int(input('How many drinks have been stocked? > '))
        drinkMachine.purchase(drinksToBuy)
        drinkMachine.restock(bottlesToStock)
        drinkMachine.report()
    else:
        return runMain()
    runAgain()

if __name__ == "__main__":
    runMain()
