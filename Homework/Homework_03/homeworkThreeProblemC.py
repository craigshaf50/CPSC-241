# -*- coding: utf-8 -*-
####################################################
# Homework 3 Problem C
# author: Craig Shaffer
# date revision: 11/13/20
# course: CPSC 241
#
# code to create a list of odd numbers and print the list
#
# input - user input numbers or done
# output - each odd num will be saved in a list and printed
#
####################################################

#empty list to store user inputs
oddNumbers=[]

#infinite loop to continue gaining user inputs
while(True):
    num=input("Enter an odd number or done >> ")
    if (num=='done'): #checks for 'done'
        print(oddNumbers)
        break #stops loop
    else:
        if(int(num)%2==1): #checks if the input is odd
            oddNumbers.append(int(num)) #adds odd num to list