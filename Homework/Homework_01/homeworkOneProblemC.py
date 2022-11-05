####################################################
#Homework 1
#author - swamy ponpandi
#date last revised - 9/3/2020
#
#code to compute the square root of a number
#using successive approximation
#
#inputs - number whose square root is to be found
#         lower perfect square
#        upper perfect square
# example - number whose root to be found = 30
#           lower perfect square = 5 (5*5 = 25)
#           upper perfect square = 6 (6*6 = 36)
#         25 < 30 < 36
####################################################

#enter the number whose square root is to be found
#input function will convert input from console to
#a string
#int function will covert string to integer

sqRootNum = int(input("enter the number : "));

print("<<Enter two perfect square roots>>");

#enter the lower and upper root
lowRoot = int(input("lower square root : "));

upperRoot = int(input("upper square root : "));

#guessed root is average of lower and upper root
guessRoot = (lowRoot + upperRoot)/2
#compute the error in the estimate
Error = guessRoot ** 2 - sqRootNum

print("First guess square root : ", guessRoot, " Error : ", 
      Error)

########### WRITE YOUR CODE BELOW  #################
#Compute the two next guess for square root
#see slides 19, 20, 22
#Print the next two guessed root and the error
####################################################
# Homework 1c
# author: Craig Shaffer
# date revision: 9/13/20
# course: CPSC 241
#
# code to compute next two guessed root and error
#
####################################################

#Determine the error of the upper and lower root
upperError=sqRootNum-(upperRoot**2)
lowError=sqRootNum-(lowRoot**2)

#Calculates guessRoot_2 based on the which initial root has the lower error
#the absolute value function allows the program to accurately compare error
if (abs(upperError) <= abs(lowError)): 
    guessRoot_2 = (upperRoot+guessRoot)/2
else:
    guessRoot_2 = (lowRoot+guessRoot)/2
    
#Calculates the asolute value of error of guessRoot_2
error_2 = abs((guessRoot_2 ** 2) - sqRootNum)

#Prints the value of the second guess root and the error
print("Second guess square root : ", guessRoot_2, " Error : ", error_2)

#Calculate guess root 3 with guessRoot and guessRoot_2
guessRoot_3 = (guessRoot+guessRoot_2)/2

#Calculate the absolute value of error of guessRoot_3
error_3 = abs((guessRoot_3**2) - sqRootNum)

#Prints the value of the third guess root and the error
print("Third guess square root : ", guessRoot_3, " Error : ", error_3)

