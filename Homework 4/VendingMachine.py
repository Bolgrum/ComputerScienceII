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
    def __init__(self, name):
        file = open(name + '.txt', 'r')
        contents = file.read()
        self.bottles = int(contents)
        self.name = name
        
    def checkStock(self):
        print(self.name + ': ' + str(self.bottles))  
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def getInventory(self):
        return self.bottles
        
    def report(self):
        with open(self.name + '.txt', 'w') as f:
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
    venderCocaCola1 = VendingMachine("CocaCola1")
    venderCocaCola2 = VendingMachine("CocaCola2")
    venderCokeZero = VendingMachine("CokeZero")
    venderDietCoke1 = VendingMachine("DietCoke1")
    venderDietCoke2 = VendingMachine("DietCoke2")
    venderSprite = VendingMachine("Sprite")
    venderFanta = VendingMachine("Fanta")
    venderDasani = VendingMachine("Dasani")
    
    userChoice = input('Would you like to (A) check stock or (B) generate report? (A/B) > ')
    
    if userChoice.lower() == 'a':
        venderCocaCola1.checkStock()
        venderCocaCola2.checkStock()
        venderCokeZero.checkStock()
        venderDietCoke1.checkStock()
        venderDietCoke2.checkStock()
        venderSprite.checkStock()
        venderFanta.checkStock()
        venderDasani.checkStock()
    elif userChoice.lower() == 'b':
        try:
            drinksToBuyCocaCola1 = int(input('How many drinks have been bought from CocaCola1: > '))
            if drinksToBuyCocaCola1 > 50:
                print("Value cannot be greater than 50.")
                return runMain()
            drinksToBuyCocaCola2 = int(input('How many drinks have been bought from CocaCola2: > '))
            if drinksToBuyCocaCola2 > 50:
                print("Value cannot be greater than 50.")
                return runMain()
            drinksToBuyCokeZero = int(input('How many drinks have been bought from CokeZero: > '))
            if drinksToBuyCokeZero > 50:
                print("Value cannot be greater than 50.")
                return runMain()
            drinksToBuyDietCoke1 = int(input('How many drinks have been bought from DietCoke1: > '))
            if drinksToBuyDietCoke1 > 50:
                print("Value cannot be greater than 50.")
                return runMain()
            drinksToBuyDietCoke2 = int(input('How many drinks have been bought from DietCoke2: > '))
            if drinksToBuyDietCoke2 > 50:
                print("Value cannot be greater than 50.")
                return runMain()
            drinksToBuySprite = int(input('How many drinks have been bought from Sprite: > '))
            if drinksToBuySprite > 50:
                print("Value cannot be greater than 50.")
                return runMain()
            drinksToBuyFanta = int(input('How many drinks have been bought from Fanta: > '))
            if drinksToBuyFanta > 50:
                print("Value cannot be greater than 50.")
                return runMain()
            drinksToBuyDasani = int(input('How many drinks have been bought from Dasani: > '))
            if drinksToBuyDasani > 50:
                print("Value cannot be greater than 50.")
                return runMain()
            else:
                print("")
                bottlesToStockCocaCola1 = int(input('How many CocaCola have been stocked? > '))
                if (50 - drinksToBuyCocaCola1 + bottlesToStockCocaCola1) > 50:
                    print("Total cannot exceed 50.")
                    return runMain()
                bottlesToStockCocaCola2 = int(input('How many CocaCola have been stocked? > '))
                if (50 - drinksToBuyCocaCola2 + bottlesToStockCocaCola2) > 50:
                    print("Total cannot exceed 50.")
                    return runMain()
                bottlesToStockCokeZero = int(input('How many CokeZero have been stocked? > '))
                if (50 - drinksToBuyCocaCola2 + bottlesToStockCokeZero) > 50:
                    print("Total cannot exceed 50.")
                    return runMain()
                bottlesToStockDietCoke1 = int(input('How many DietCoke have been stocked? > '))
                if (50 - drinksToBuyCocaCola2 + bottlesToStockDietCoke1) > 50:
                    print("Total cannot exceed 50.")
                    return runMain()
                bottlesToStockDietCoke2 = int(input('How many DietCoke have been stocked? > '))
                if (50 - drinksToBuyCocaCola2 + bottlesToStockDietCoke2) > 50:
                    print("Total cannot exceed 50.")
                    return runMain()
                bottlesToStockSprite = int(input('How many Sprite have been stocked? > '))
                if (50 - drinksToBuyCocaCola2 + bottlesToStockSprite) > 50:
                    print("Total cannot exceed 50.")
                    return runMain()
                bottlesToStockFanta = int(input('How many Fanta have been stocked? > '))
                if (50 - drinksToBuyCocaCola2 + bottlesToStockFanta) > 50:
                    print("Total cannot exceed 50.")
                    return runMain()
                bottlesToStockDasani = int(input('How many Dasani have been stocked? > '))
                if (50 - drinksToBuyCocaCola2 + bottlesToStockDasani) > 50:
                    print("Total cannot exceed 50.")
                    return runMain()
        except:
            print("You need to enter an integer for stock values.")
            runMain()
        print("")
        venderCocaCola1.purchase(drinksToBuyCocaCola1)
        venderCocaCola1.restock(bottlesToStockCocaCola1)
        venderCocaCola2.purchase(drinksToBuyCocaCola2)
        venderCocaCola2.restock(bottlesToStockCocaCola2)
        venderCokeZero.purchase(drinksToBuyCokeZero)
        venderCokeZero.restock(bottlesToStockCokeZero)
        venderDietCoke1.purchase(drinksToBuyDietCoke1)
        venderDietCoke1.restock(bottlesToStockDietCoke1)
        venderDietCoke2.purchase(drinksToBuyDietCoke2)
        venderDietCoke2.restock(bottlesToStockDietCoke2)
        venderSprite.purchase(drinksToBuySprite)
        venderSprite.restock(bottlesToStockSprite)
        venderFanta.purchase(drinksToBuyFanta)
        venderFanta.restock(bottlesToStockFanta)
        venderDasani.purchase(drinksToBuyDasani)
        venderDasani.restock(bottlesToStockDasani)
        
        print("Report follows:")
        venderCocaCola1.report()
        venderCocaCola2.report()
        venderCokeZero.report()
        venderDietCoke1.report()
        venderDietCoke2.report()
        venderSprite.report()
        venderFanta.report()
        venderDasani.report()
    else:
        return runMain()
    runAgain()

if __name__ == "__main__":
    brands = ['CocaCola1', 'CocaCola2', 'CokeZero', 'DietCoke1', 'DietCoke2', 'Sprite', 'Fanta', 'Dasani']    
    runMain()
