

#problem1.py
#Exam 1 - Cpsc241
#
#the code below asks the user to input his/her ID
#check if the ID is valid or not
#print an appropriate message

######### INSTRUCTIONS ####################
#there are several errors in the code
#identify and fix the errors
#write brief comments about how you fixed each error
####################################################
# Exam 1 Problem 1
# author: Craig Shaffer
# date revision: 9/25/20
# course: CPSC 241
#
# Fix the errors
#
####################################################

myId = int(input("enter your ID : ")) #variable error. Instead of %myID I used myID
#the input prompts for score instead of ID so I changed that as well

if(myId == 2345): #because of the variable error earlier I had to make the same change here
#I also had to add another = in order to compare myId to 2345. Syntax error

    print("Id is valid. Welcome!!") #indentation error. it had no indentation
    
else: #needed a colon after else. Syntax error
    print("Invlaid Id. Retry again!!!")
    