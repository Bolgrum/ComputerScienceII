# Homework 7.3                      ParseFood.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 10/15/2021

# 28.1 LAB: Parsing food data
# Given a text file containing the availability of food items, 
# write a program that reads the information from the text file 
# and outputs the available food items. The program first reads 
# the name of the text file from the user. The program then reads 
# the text file, stores the information into four separate lists, 
# and outputs the available food items in the following format: 
# name (category) -- description
#
# Assume the text file contains the category, name, description, 
# and availability of at least one food item, separated by a tab 
# character ('\t').
#
# Ex: If the input of the program is:
#
# food.txt
# and the contents of food.txt are:
#
# Sandwiches Ham sandwich Classic ham sandwich Available
# Sandwiches Chicken salad sandwich Chicken salad sandwich Not available
# Sandwiches Cheeseburger Classic cheeseburger Not available
# Salads Caesar salad Chunks of romaine heart lettuce dressed with lemon juice Available
# Salads Asian salad Mixed greens with ginger dressing, sprinkled with sesame Not available
# Beverages Water 16oz bottled water Available
# Beverages Coca-Cola 16oz Coca-Cola Not available
# Mexican food Chicken tacos Grilled chicken breast in freshly made tortillas Not available
# Mexican food Beef tacos Ground beef in freshly made tortillas Available
# Vegetarian Avocado sandwich Sliced avocado with fruity spread Not available
# the output of the program is:
#
# Ham sandwich (Sandwiches) -- Classic ham sandwich
# Caesar salad (Salads) -- Chunks of romaine heart lettuce dressed with lemon juice
# Water (Beverages) -- 16oz bottled water
# Beef tacos (Mexican food) -- Ground beef in freshly made tortillas

column1 = []
column2 = []
column3 = []
column4 = []

inputFileName = input("Please input file name: > ")
f = open(inputFileName)

for row in f:
    field = row[:-1].split('\t')
    column1.append(field[0])
    column2.append(field[1])
    column3.append(field[2])
    column4.append(field[3])

for row in range(len(column4)):
    if column4[row] == "Available":
        print(column2[row] + " (" + column1[row] + ") -- " + column3[row])