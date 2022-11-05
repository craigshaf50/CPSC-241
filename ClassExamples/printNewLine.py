# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:28:20 2020

@author: craig
"""
'''
#introduces new line

print("welcome ")
print("to the class")

#does not introduce new line

print("welcome ", end=" ")
print("to the class")
'''

'''
i=0
numChar=int(input("Enter the number of characters>>"))
while (i<numChar):
     char=input("Enter the character>>")
     if i%2 == 0:
         print(char)
     i=i+1
'''
i=0
xAlt=0

numTerms=float(input("Enter the number of terms to compute: "))
x=float(input("Enter the value of x: "))

while(i<numTerms):
    i=i+1
    if(i!=1):
        x=-x
    xAlt=xAlt+(x/i)
    print(xAlt)
        
         