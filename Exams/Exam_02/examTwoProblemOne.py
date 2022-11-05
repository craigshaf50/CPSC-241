# -*- coding: utf-8 -*-
####################################################
# Exam 2 Problem 1
# author: Craig Shaffer
# date revision: 11/02/20
# course: CPSC 241
#
# code to print N numbers in the Fibonacci sequence
#
# input - How many numbers (N) of the series the 
#         user wishes to print
#
# output - N numbers of the Fibonacci sequence
#
####################################################

N=int(input("Enter the amount of numbers you wish to generate >> "))

#initialize variables
num1=0 
num2=1
sum=0
i=1 #loop counter

#tells the user what will be printed
print("The Fibonacci Sequence for ", N, " numbers: ")

#while loop to generate sequence
while(i<=N):  #while i is less than or equal to N the loop will continue  
  print(sum) #prints the value of sum
  i=i+1 #updates loop counter
  #reassign values of num1 and num2
  num1=num2 
  num2=sum
  sum=num1+num2 #updates the value of the sum
