# -*- coding: utf-8 -*-
####################################################
# Homework 3 Problem A
# author: Craig Shaffer
# date revision: 11/13/20
# course: CPSC 241
#
# code to print months and their index with while loop
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

#While index is less than the length of list
while(i<len(months)):
    print("The index for ", months[i], " is ", i) #prints each month and its index
    i=i+1 #Update loop counter


