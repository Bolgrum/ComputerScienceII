# Homework 7.1                      WordFrequencies.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 10/15/2021

# 12.9 LAB: Word frequencies (lists)
# Write a program that first reads in the name of an input file 
# and then reads the file using the csv.reader() method. The 
# file contains a list of words separated by commas. Your program 
# should output the words and their frequencies (the number of 
# times each word appears in the file) without any duplicates.
#
# Ex: If the input is:
#
# input1.csv
# and the contents of input1.csv are:

# hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
# the output is:
# hello 1
# cat 2
# man 2
# hey 2
# dog 2
# boy 2
# Hello 1
# woman 1
# Cat 1
# Note: There is a newline at the end of the output, and 
# input1.csv is available to download.

import csv

fileName = input("Please input file name: > ")

wordList = []

with open(str(fileName), 'r') as csvfile:
    userFile = csv.reader(csvfile, delimiter=',')
    
    for row in userFile:
        for index in range(len(row)):
            if row[index] not in wordList:
                print(f'{row[index]} {row.count(row[index])}')
                wordList.append(row[index])