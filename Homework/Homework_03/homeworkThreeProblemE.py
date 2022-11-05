# -*- coding: utf-8 -*-
####################################################
# Homework 3 Problem E
# author: Craig Shaffer
# date revision: 11/13/20
# course: CPSC 241
#
# code concatenate the user's inputs
#
# input - user can input any data or done
# output - the inputs will added to a list 
#          and then be concatenated in a string
#
####################################################

#empty list to store data
inputList=[]

#initialize an empty variable to hold concatenated string
inputString=''

#infinite loop to get user input
while(True):
    userInput=input("Enter any data (float, int, string) >> ")
    if (userInput=='done'): #checks for 'done'
        break #stops loop
    inputList.append(userInput) #adds user input to list

#iterates through the items in the list and concatenates them
for item in inputList:
    inputString=inputString + str(item) #concatenates each item into inputString

#prints the concatenated string
print(inputString)
    

