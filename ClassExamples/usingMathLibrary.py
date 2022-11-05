# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:24:18 2020

@author: craig
"""
import math

#roots of a quadratic equation
#   a b c
def sqrt(f,g,h):
    d = (g**2)-4*f*h
    if d<0:
        print("there are no real roots")
    else: 
        root1=(-g + math.sqrt(d))/(2*f)
        root2=(-g - math.sqrt(d))/(2*f)
        print("root1 = ", root1, "root2 = ", root2)


a=int(input("enter a >> "))
b=int(input("enter b >> "))
c=int(input("enter c >> "))

sqrt(a, b, c)