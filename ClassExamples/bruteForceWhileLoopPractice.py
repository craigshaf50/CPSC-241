# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:27:25 2020

@author: craig
"""

#check if num is perfect cube
#input positive integer N
#Does there exist an integer, X, such that X^3 = N
#BRUTE FORCE STRATEGY

#initialize variables
N = int(input("Enter the integer >> "))
X = 1 #number that will be updated and cubed to attempt to find N

while ((X**3) < N):
    X = X + 1 #updates the guess value X
    
if ((X**3) == N): #checks if the value X is eqaul to N
    print("Cube root is: ", X) 
else: #if X^3 is greater than N, there is no cube root
    print("There is no cube root")

