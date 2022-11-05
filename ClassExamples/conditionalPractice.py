# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:03:39 2020

@author: craig
"""

#get score as input, print "grade is A" if score is at least 90

#get score and convert to int data type
'''score=input("enter your score >> ")
score=int(score)

if (score>=90):
    print("your grade is A") #only if grade is >= 90, then execute
    print("congrats!")
elif (score>=80) and (score<90): #checks if statement is true
    print("your grade is B")
elif (score>=70) and (score<80):
    print("your score is C")
elif (score>=60) and (score<70):
    print("your score is D")
else:
    print("contact your instructor because you are failing") #default statement
'''    
   
x = int(input("enter x : "))
y = int(input("enter y : "))
Z = int(input("enter Z : "))

if (Z == 0):
    print("The sum of x and y is ", x+y)
elif (Z == 1):
    print("The product of x and y is ", x*y)
elif (Z == 2):
    print ("The mod of x and y is ", x%y)
else:
    print("Z must be 0, 1, 2")