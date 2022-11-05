# -*- coding: utf-8 -*-
####################################################
# Homework 1b
# author: Craig Shaffer
# date revision: 9/13/20
# course: CPSC 241
#
# code to switch the contents of two variables
#
# input - two integers assigned to two variables
# output - two variables with swapped contents
#
####################################################
print("Switch the contents of two variables")

#Prompts user for two integers for var_A and var_B. Converts to int type
#Prints the values of var_A and var_B prior to the switch
var_A=int(input("Enter the value for var_A >> "))
var_B=int(input("Enter the value for var_B >> "))
print("Prior to switching, var_A is ", var_A, " and var_B is ", var_B)

#Switch the contents with a temporary variable - tempVar
tempVar=var_A #stores the contents of var_A
var_A=var_B #var_A gains the contents of var_B
var_B=tempVar #var_B gains the contents of var_A that were stored in tempVar

#Prints the swapped contents of var_A and var_B
print("After switching, var_A is ", var_A, "and var_B is ", var_B)
