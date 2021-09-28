# Homework 5.1                      ExceptionHandlingInputStringVsInteger.py
# Version:                          v1.0.1
# Completed by:                     Anthony Braden on 09/24/2021

# 10.8 LAB: Exception handling to detect input string vs. integer
# The given program reads a list of single-word first names and ages 
# (ending with -1), and outputs that list with the age incremented. The 
# program fails and throws an exception if the second input on a line is a 
# string rather than an integer. At FIXME in the code, add try and except 
# blocks to catch the ValueError exception and output 0 for the age.

# Ex: If the input is:

# Lee 18
# Lua 21
# Mary Beth 19
# Stu 33
# -1
# then the output is:

# Lee 19
# Lua 22
# Mary 0
# Stu 34

def gatherInput(name, age):
    parts = input('Please insert a name and age separated by a space: > ').split()
    return parts

def separateNameAge(name, age, parts):
    i = 0
    name.append(parts[i])
    while i+1 != len(parts)-1:
        name[len(name)-1] = name[len(name)-1] + ' ' + parts[i+1]
        i += 1
    age.append(int(parts[len(parts) - 1]) + 1)
    
def printResults(name, age):
    for i in range(len(name)):
        print(f'{name[i]} {age[i]}') 

def printToFile(name, age):
    printToFile = input("Would you like to export your list to a .csv file? (Y/N)? > ") 
    if(printToFile.lower() == "y"):
        fileName = input("Please insert file name: > ") + ".csv"
        with open(fileName, 'a', newline='') as f:
            for i in range(len(name)):
                string = name[i] + ' ' + str(age[i]) + '\n'
                f.write(string)
    elif(printToFile.lower() == "n"):
        pass
    else:
        return runAgain()    

def runAgain():
    startAgain = input("Would you like to fill another name/age list? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Exiting program.")
        exit()
    else:
        return runAgain()

def runMain():
    name = []
    age = []
    parts = gatherInput(name, age)
    while parts[0] != "-1":
        separateNameAge(name, age, parts)
        parts = gatherInput(name, age)
    print(name)
    print(age)
    printResults(name, age)
    printToFile(name, age)
    runAgain()

if __name__ == '__main__':    
    runMain()