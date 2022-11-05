# -*- coding: utf-8 -*-
####################################################
# Homework 3 Problem D
# author: Craig Shaffer
# date revision: 11/13/20
# course: CPSC 241
#
# code to create/print a list of odd numbers and print the sum
#
# input - user inputs numbers or done
# output - each odd num will be saved in a list and 
#          be printed with the sum of the values in 
#          the list 
#
####################################################

#empty list to store user inputs
oddNumbers=[]

#initialize variable to store sum of odd numbers
sum=0

#infinite loop to continue gaining user inputs
while(True):
    num=input("Enter an odd number or done >> ")
    if (num=='done'): #checks for 'done'
        print(oddNumbers)
        print("The sum of the values in list oddNumbers is ", sum)
        break #stops loop
    else:
        if(int(num)%2==1): #checks if the input is odd
            oddNumbers.append(int(num)) #adds odd num to list
            sum=sum+int(num) #updates value of sum by adding the odd number