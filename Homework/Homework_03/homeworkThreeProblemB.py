# -*- coding: utf-8 -*-
####################################################
# Homework 3 Problem B
# author: Craig Shaffer
# date revision: 11/13/20
# course: CPSC 241
#
# code to print months and their index with for loop
#
# input - list of months in a year
# output - print each item and its index
#
####################################################


#list of months
months=["January", "February", "March", "April", "May",
        "June", "July", "August", "September", "October",
        "November", "December"]

i=0 #loop counter/index

#for loop accesses each month in the list of months and
#prints the month and its index
for month in months:
    print("The index for ", month, " is ", i)
    i=i+1 #updates index/loop counter
    
