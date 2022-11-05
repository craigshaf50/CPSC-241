# -*- coding: utf-8 -*-
####################################################
# Homework 2 Problem A
# author: Craig Shaffer
# date revision: 9/27/20
# course: CPSC 241
#
# code to find largest odd number
#
# input - 4 integers
# output - largest odd number
#
####################################################

#get four numbers, determine the largest odd number
#print message if none is odd

a = input("enter the first number >> ")
a = int(a)

b = input("enter the second number >> ")
b = int(b)

c = input("enter the third number >> ")
c = int(c)

d = input("enter the fourth number >> ")
d = int(d)

#four integer variables used as placeholders for 
#the largest, middle largest, and middle lowest and lowest number
largest = 0
midLarge = 0
midLow = 0
lowest = 0

#examine the first two numbers - a,b and determine the largest
#assign value to place holder accordingly
if(a >= b):
    largest, midLarge = a, b
else:
    largest, midLarge = b, a

#examines where c compares to the first two values
if(c >= midLarge):
   midLarge, midLow = c, midLarge #if c is bigger. midLarge and c swap
   if(midLarge >= largest): #if midLarge is bigger than largest they swap
      largest, midLarge = midLarge, largest
else: #if c is lower than midLarge and largest
    midLow = c #c is third highest value currently
    
#examines where d fits with previous three values
if(d >= midLow): 
    midLow, lowest = d, midLow #if d is bigger than midLow. swap d and midLow
    if(midLow >= midLarge):
        midLarge, midLow = midLow, midLarge #if midLow is bigger than midLarge swap
        if(midLarge >= largest):
            largest, midLarge = midLarge, largest #if midLarge is bigger than largest swap
else:
     lowest = d #d is the smallest value

#print the values in order
print("The values in order are: ", largest, midLarge, midLow, lowest)

#determine largest odd number with mod function
if(largest%2 == 1):
   print("largest odd number is ", largest)
elif(midLarge%2 == 1):
   print("largest odd number ", midLarge)
elif(midLarge%2 == 1):
   print("largest odd number ", midLow)
elif(lowest%2 == 1):
   print("largest odd number ", lowest)
else: #no odd numbers entered
   print("there are no odd numbers in the input")
