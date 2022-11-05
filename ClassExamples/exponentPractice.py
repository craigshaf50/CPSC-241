# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:19:11 2020

@author: craig
"""

# e=2.71828
# get the value of X - floating point number


X=input("input the value of X >> ")
X=float(X) # converts X to a float type

# expression used for e^X
e_X= 1 + X + (X**2)/(1*2) + (X**3)/(1*2*3) + (X**4)/(1*2*3*4)

# print e^X
print("e raised to the power of X: X= ", X, " is ", e_X)



