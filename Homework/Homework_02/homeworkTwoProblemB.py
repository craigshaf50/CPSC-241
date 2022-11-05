# -*- coding: utf-8 -*-
####################################################
# Homework 2 Problem B
# author: Craig Shaffer
# date revision: 9/27/20
# course: CPSC 241
#
# code to find the root and power of the integer
#
# input - integer
# output - root and power of integer (can be multiple)
#
####################################################

#prompts user for integer
integer = int(input("Enter an integer >> "))

#initializes value of root and pwr
root = 0
pwr = 0

#while loop until root**pwr>=integer
while root**pwr < abs(integer):
    root = root + 1 #updates root 
    while pwr < 6: #checks pwr from values 0 to 6
        pwr = pwr + 1 #updates pwr and acts as loop counter
        if root**pwr == integer: #if root**pwr==integer print root and pwr
            print("Root is:", root, ", Power is:", pwr)
    if root == integer: 
        break #if root == integer stop the loop
    pwr = 0 #reset power to continue checking
   
#technically there is always a root and power combination for every number
#the root just ends up as the integer to the power of one
#however, if you want to exclude that answer, use the code below


'''
integer = int(input("Enter an integer >> "))
root = 0
pwr = 0
#counts number of roots, if number of roots is zero
#then the only root is integer**1 which is what we are excluding
count = 0

#while loop until root**pwr>=integer
while root**pwr < abs(integer):
    root = root + 1 #updates root 
    while pwr < 6: #checks pwr from values 0 to 6
        pwr = pwr + 1 #updates pwr and acts as loop counter
        if root**pwr == integer and root != integer: #if root**pwr==integer print root and pwr
            count = count + 1 #updates the count
            print("Root is:", root, ", Power is:", pwr)
        if root == integer and count==0: #if count == 0 then the only root is integer**1.
                                         #we are excluding this root in this code
            print("No such pair of integers exists") #print no pairs exist
            break #stops loop
    if root == integer: 
        break #if root == integer stop the loop
    pwr = 0 #reset power to continue checking
'''







