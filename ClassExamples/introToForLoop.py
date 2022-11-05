# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:59:21 2020

@author: craig
"""
'''
#variable i is going to take the values
#provided by the range function
#the value provided by the range function is copied into
#variable i
totalScore=0

for i in range(0,7): #0,1,2,3,4,5,6
    if (i==2 or i==4):
        pass #skips over student 2&4
    else:
        print("Student ", i)
        score = int(input("enter your score of student : ")) 
        totalScore= totalScore + score
    
print("total score is ", totalScore)
'''
'''
for i in range(0,7):
   # print("****** i is: ", i)
    for j in range(0,5): #row in matrix
        print(j, end=" ")
    print("\n", end=" ") #print new line
'''
x= 0.0

for i in range(10):
    x=x+.1
if (abs(x - 1.0) < 0.0001):
        print("x is 1.0")
else:
        print("x is not 1.0")
        