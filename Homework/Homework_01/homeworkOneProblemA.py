# -*- coding: utf-8 -*-
####################################################
# Homework 1a
# author: Craig Shaffer
# date revision: 9/13/20
# course: CPSC 241
#
# code to compute area of a circle
#
# input - radius
# output - area of a circle
#
####################################################
print("Compute the area of a circle")

#Prompts the user for radius and converts it to float type
radius=input("Enter the radius of the circle >> ")
radius=float(radius)

#Calculates area with the formula Area=pi*(radius^2) when pi=3.14
#then prints the area of the circle
area= 3.14 * (radius**2)
print("The area of the circle with a radius of ", radius, " is ", area, 
      " units squared.")
