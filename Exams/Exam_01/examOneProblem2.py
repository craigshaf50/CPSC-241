# -*- coding: utf-8 -*-
####################################################
# Exam 1 Problem 2
# author: Craig Shaffer
# date revision: 9/25/20
# course: CPSC 241
#
# code to find sum of odd numbers and even numbers
#
# input - odd and even numbers or 'done' to stop
# output - sum of odd and even numbers separately
#
####################################################

#initialize variables to hold sum of odd and even values
oddSum=0 
evenSum=0

#infinite loop to ask for numbers
while(True):
    #gets input for numVal
    numVal = input("enter the number or done >> ")
    
    if(numVal == "done"): #determines what to print for odd and even sum
        if(oddSum == 0): 
            print("no odd numbers were input")
        else:
            print("sum of odd numbers is: ", oddSum)
        if(evenSum == 0):
            print("no even numbers were input")
        else:
            print("sum of even numbers is: ", evenSum)
        break #stops infinite loop
        
    numVal = int(numVal) #converts string numVal to int type
    
    if((numVal % 2) != 0): #checks if numVal is odd
        oddSum = oddSum + numVal #updates oddSum
        
    else: #if numVal is not odd it is even
        evenSum = evenSum + numVal #updates evenSum
    
