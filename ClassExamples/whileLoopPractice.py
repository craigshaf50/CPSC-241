# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:29:09 2020

@author: craig
"""
#practice
'''numItr = int(input("enter number of iteration >> "))

i=0 #loop counter
while (i<numItr):
    i=i+1 #updating loop counter
    print("Iteration #", i, " hello")
print("End of while loop")
'''
#initialize variables
numItr=5 #number of iterations
i=0 #loop counter
maxOdd=0
curInp=0

#while loop to determine the largest odd number
while(i<numItr):
    curInp=int(input("Enter number >> "))
    if (curInp % 2) != 0:
        if (curInp > maxOdd):
            maxOdd = curInp
    i = i + 1 #update the loop counter

#print maxOdd or no odd number
if (maxOdd != 0):
    print("The largest odd number is: ", maxOdd)
else:
    print("There is no odd number")