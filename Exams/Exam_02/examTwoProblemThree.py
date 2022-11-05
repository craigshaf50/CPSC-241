# -*- coding: utf-8 -*-
####################################################
# Exam 2 Problem 3
# author: Craig Shaffer
# date revision: 11/02/20
# course: CPSC 241
#
# code to print woof woof when user inputs "pooch"
#
# input - characters or done
# output - if pooch is entered, woof woof will be printed
#
####################################################

#initialize flags - will change to one if found
foundP=0
foundO=0
foundC=0
foundH=0

while(True): #infinite loop
    char=input("Enter the next character or done: ")
    if char=='done': #if 'done' is entered, stop loop
        break
    if char=='p': #checks for p
        foundP=1
    elif (char=='o') and (foundP==1): #checks for o after p
        foundO=foundO+1
    elif (char=='c') and (foundO==2): #checks for c after 2 o's 
        foundC=1
    elif (char=='h') and (foundC==1): #checks for h after c
        print("woof woof") 
    else: #resets the flags and continues search for 'pooch'
        foundP=0
        foundO=0
        foundC=0
        foundH=0

