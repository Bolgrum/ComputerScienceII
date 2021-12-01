# Homework 7.2                      SortTV.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 10/15/2021

# 12.10 LAB: Sorting TV Shows (dictionaries and lists)
# Write a program that first reads in the name of an input file 
# and then reads the input file using the file.readlines() method. 
# The input file contains an unsorted list of number of seasons 
# followed by the corresponding TV show. Your program should put 
# the contents of the input file into a dictionary where the number 
# of seasons are the keys, and a list of TV shows are the values 
# (since multiple shows could have the same number of seasons).
#
# Sort the dictionary by key (least to greatest) and output the 
# results to a file named output_keys.txt. Separate multiple TV 
# shows associated with the same key with a semicolon (;), ordering 
# by appearance in the input file. Next, sort the dictionary by 
# values (alphabetical order), and output the results to a file 
# named output_titles.txt.
#
# Ex: If the input is:
#
# file1.txt
# and the contents of file1.txt are:
#
# 20
# Gunsmoke
# 30
# The Simpsons
# 10
# Will & Grace
# 14
# Dallas
# 20
# Law & Order
# 12
# Murder, She Wrote
# the file output_keys.txt should contain:
#
# 10: Will & Grace
# 12: Murder, She Wrote
# 14: Dallas
# 20: Gunsmoke; Law & Order
# 30: The Simpsons
# and the file output_titles.txt should contain:
# 
# Dallas
# Gunsmoke
# Law & Order
# Murder, She Wrote
# The Simpsons
# Will & Grace
# Note: There is a newline at the end of each output file, 
# and file1.txt is available to download.

fileName = input("Please input file name: > ")

userFile = open(str(fileName))

outputFile = userFile.readlines()

TVDictionary = {}
showList = []
splitShowList = []

for index in range(len(outputFile)):
    tempList = []
    listObject = outputFile[index].strip('\n')
    if (index + 1 < len(outputFile) and (index % 2 == 0)):
        if int(listObject) in TVDictionary:
            TVDictionary[int(listObject)].append(outputFile[index + 1].strip('\n'))
        else:
            tempList.append(outputFile[index + 1].strip('\n'))
            TVDictionary[int(listObject)] = tempList

dictionarySortedByKeys = dict(sorted(TVDictionary.items()))

for x in TVDictionary.keys():
    showList.append(TVDictionary[x])

for x in showList:
    for i in x:
        splitShowList.append(i)

splitShowList = sorted(splitShowList)

f = open('OutputKeys.txt', 'w')
for key, value in dictionarySortedByKeys.items():
    f.write(str(key) + ": ")
    for item in value[:-1]:
        f.write(item + "; ")
    f.write(value[-1])
    f.write("\n")
f.close()

f = open('Titles.txt', 'w')
for item in splitShowList:
    f.write(item + '\n')
f.close()