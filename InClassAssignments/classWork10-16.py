# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:29:33 2020

@author: craig
"""

i=0
xAlt=0
c=-1 #starting coefficient. Will be 1 before used to compute term

numTerms=float(input("Enter the number of terms to compute: "))
x=float(input("Enter the value of x: "))

while(i<numTerms):
    i=i+1
    c=c+2 #updates coefficient
    if (i%2 != 0):
        xAlt=xAlt+(c)*x #odd i
    else:
        xAlt=xAlt-(c)*(x**2) #even i

print(xAlt)
