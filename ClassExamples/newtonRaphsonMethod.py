# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:42:39 2020

@author: craig
"""


#solve x^3 = k using Newton-Raphson method
#f(x) = x^3-k
#first derivative g(x) = 3x^2


K=float(input("enter K >> "))

guessRoot = (float(input("initial guess root >> ")))

accuracy=0.001

while(True):
    if(abs(guessRoot**3 - K) < accuracy):
        print("root is: ", guessRoot)
        break
    guessRoot=guessRoot - ((guessRoot**3 - K)/(3 * (guessRoot**2)))