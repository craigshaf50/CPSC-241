# -*- coding: utf-8 -*-
####################################################
# Exam 2 Problem 2
# author: Craig Shaffer
# date revision: 11/02/20
# course: CPSC 241
#
# code to compute the mathematical series (F) to N terms
#
# input - user will enter values for x, y, N
#
# output - F will be printed to N number of terms
#
####################################################

#get N,x,y fromt the user
N=int(input("Please enter the number of terms >> "))
x=float(input("Please enter the value of x >> "))
y=float(input("Please enter the value of y >> "))

F=0 #initialize F
base=2 #initialize base/denominator

i=0 #loop counter

#loop to find value of F
while(i<N): 
    if(i==0):
        F=(x*y) #update F for first iteration
        i=i+1 #update loop counter
    else:
        F=F+((x/base)*(y/(base+1)))
        i=i+1 #updates loop counter
        base=base+2 #updates base by 2
    print(F)
print("F for ", N, " number of terms is: ", F)    
        
    
