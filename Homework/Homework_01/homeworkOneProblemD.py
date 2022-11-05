# -*- coding: utf-8 -*-
####################################################
# Homework 1d
# author: Craig Shaffer
# date revision: 9/13/20
# course: CPSC 241
#
# code to duplicate a string a certain amount of times
#
# input - string, number of duplications(N)
# output - duplicated string
#
####################################################
print("Enter a message you wish to duplicate")

#Prompt the user for a string
string=input("Type your message here >> ")
string=string + " " #added space to separate messages/words

#Prompt the user to enter the number of duplications
N=int(input("Enter the number of dulpications >> "))

#Duplicate the string N times and save the duplicated string in dupString
#Print dupString
dupString=string*N #multiplies string by N
print(dupString)

