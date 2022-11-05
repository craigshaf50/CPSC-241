# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:24:54 2020

@author: craig
"""

#Determine the sqaure root of N through approximation
#BRUTE FORCE

N=float(input("enter the input >> "))

root = 1.0

accuracy = 0.0001

step = 0.00001

while(True):
    if(abs(root**2 - N) < accuracy):
        print("root is: ", root)
        break

    root = root + step


