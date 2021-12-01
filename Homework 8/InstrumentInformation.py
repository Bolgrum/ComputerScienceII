# Homework 8.1                      InstrumentInformation.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 10/29/2021

# 13.8 LAB: Instrument information (derived classes)
# Given the base class Instrument, define a derived class 
# StringInstrument for string instruments.
#
# Ex: If the input is:
#
# Drums
# Zildjian
# 2015
# 2500
# Guitar
# Gibson
# 2002
# 1200
# 6
# 19
# the output is:
# 
# Instrument Information:
# Name: Drums
# Manufacturer: Zildjian
# Year built: 2015
# Cost: 2500
# Instrument Information:
# Name: Guitar
# Manufacturer: Gibson
# Year built: 2002
# Cost: 1200
# Number of strings: 6
# Number of frets: 19

class Instrument:
    def __init__(self, name, manufacturer, yearBuilt, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.yearBuilt = yearBuilt
        self.cost = cost
      
    def printInfo(self):
        print('\nInstrument Information:')
        print('   Name:', self.name)
        print('   Manufacturer:', self.manufacturer)
        print('   Year built:', self.yearBuilt)
        print('   Cost: $' + str(self.cost))


class StringInstrument(Instrument):
    def __init__(self, name, manufacturer, yearBuilt, cost, numberOfStrings, numberOfFrets):
        Instrument.__init__(self, name, manufacturer, yearBuilt, cost) 
        self.numberOfStrings = numberOfStrings
        self.numberOfFrets = numberOfFrets
      

if __name__ == "__main__":
    instrumentName = input('Instrument name: > ')
    manufacturerName = input('Manufacturer name: > ')
    yearBuilt = int(input('Year built: > '))
    cost = int(input('Cost: > $'))
    stringInstrumentName = input('Instrument name: > ')
    stringManufacturer = input('Manufacturer name: > ')
    stringYearBuilt = int(input('Year Built: > '))
    stringCost = int(input('Cost: > $'))
    numberOfStrings = int(input('Number of Strings: > '))
    numberOfFrets = int(input('Number of Frets: > '))
    
    myInstrument = Instrument(instrumentName, manufacturerName, yearBuilt, cost)
    myStringInstrument = StringInstrument(stringInstrumentName, stringManufacturer, stringYearBuilt, stringCost, numberOfStrings, numberOfFrets)

    myInstrument.printInfo()
    myStringInstrument.printInfo()
   
    print('   Number of strings:', myStringInstrument.numberOfStrings)
    print('   Number of frets:', myStringInstrument.numberOfFrets)