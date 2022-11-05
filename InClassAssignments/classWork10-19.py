# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:59:51 2020

@author: craig
"""

i=0 #initialize loop counter
xAlt=0 
c=-1 #starting coefficient. Will be 1 before used to compute term
exp=0 #initialize exponent

numTerms=float(input("Enter the number of terms to compute: "))
x=float(input("Enter the value of x: "))

while(i<numTerms):
    i=i+1
    c=c+2 #updates coefficient
    exp=exp+1 #update exponent
    if (i%2 != 0):
        xAlt=xAlt+(c)*(x**exp) #odd i
    else:
        xAlt=xAlt-(c)*(x**exp) #even i

print(xAlt) #prints answer