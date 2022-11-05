# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:21:43 2020

@author: craig
"""

N = int(input("enter N: "))

#N! = 1 x 2 x 3 x 4 ..... x N

#N! = N x (N-1) x (N-2) x (N-3)..... 3 x 2 x 1

factorial = 1

'''
while(N>1):
    factorial = factorial * N
    
    N=N-1
    
    print("N is: ", N)
    
print("Factorial is: ", factorial)
'''

i=1

while (i <= N):
    factorial = factorial * i
    i=i+1
    print("i is: ", i)
print("factorial is: ", factorial)

