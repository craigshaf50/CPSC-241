# -*- coding: utf-8 -*-
####################################################
# Exam 1 Problem 3
# author: Craig Shaffer
# date revision: 9/25/20
# course: CPSC 241
#
# code to find sum of consecutive even numbers
#
# input - odd and even numbers or 'done' to stop
# output - sum of consecutive even numbers
#
####################################################

#initialize variable
evenSum=0

#begins the infinite loop to continue to ask for numbers
while(True):
    numVal = input("enter the number or done >> ") #gets user input for numVal
   
    if(numVal == "done"): #checks for done to stop the loop
        print("sum of even numbers is: ", evenSum)
        break #ends infinite loop
    
    if((int(numVal))%2 != 0): #checks if input is odd
        if(evenSum != 0): #checks if evenSum has been updated
            print("sum of even numbers is: ", evenSum) #prints sum of consecutive even numbers
     
            evenSum=0 #sets evenSum to 0 because the streak of consecutive even numbers is over
   
    else: #if numVal is not odd it must be even
        evenSum = evenSum + int(numVal) #updates evenSum
        
        