# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:31:38 2020

@author: craig
"""

#get three numbers, determine the largest odd number
#print message if none are odd
num1=0
num2=0
num3=0

#step one: get three numbers from user
num1=input("enter first number >> ")
num1=int(num1)

num2=input("enter second number >> ")
num2=int(num2)

num3=input("enter third number >> ")
num3=int(num3)

#step two: sort numbers

largest=0 #num1 num2, num3 are sorted into largest, middle, and lowest
middle=0
lowest=0

if (num1>=num2):
    largest, middle = num1, num2
else:
    largest, middle = num2, num1
if (num3>=largest):
    largest, middle, lowest = num3, largest, middle    
elif (num3>=middle):
    middle, lowest = num3, middle
else:
    lowest = num3
print("The values in order are: ", largest, middle, lowest)

#step three: identify highest odd number and print
#if there is no odd number print "There is no odd number"

if (largest % 2) != 0: #checks values in order to find the largest odd num
    print("The largest odd number is: ", largest) 
elif (middle % 2) != 0:
    print("The largest odd number is: ", middle) 
elif (lowest % 2) != 0:
    print("The largest odd number is: ", lowest)
else:
    print("There is no odd number") 
