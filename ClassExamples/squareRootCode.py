# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:34:43 2020

@author: Craig
"""


# N = sqruare root of N
# lowerRoot - 
# upperRoot

N = float(input("enter the number : "))
lowerRoot = float(input("lowerRoot : "))
upperRoot = float(input("upperRoot : "))

accuracy = 0.0001 # Error < accuracy, I will stop

i = 0;

while(True):
   
   guessRoot = (lowerRoot + upperRoot)/2 # first guess

#which range will N be in  ?
# lowerRoot**2 < N < guessRoot ** 2  OR
# guessRoot**2 < N < upperRoot ** 2 
   print("root : ", guessRoot)
 
   Error = guessRoot ** 2 - N
   
   if(abs(Error) < accuracy):
      break
   
   if((guessRoot **2) > N):
      upperRoot = guessRoot
   else:
      lowerRoot = guessRoot


         