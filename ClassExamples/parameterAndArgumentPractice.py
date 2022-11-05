# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:37:40 2020

@author: craig
"""
'''
#original code

x=3
print("value is =", x)

x=7
print("value is =", x)

x=-9
print("value is =", x)
'''
'''
#subsititute a function
#y is a parameter
#x is an argument
def print_Val(y):
    print("value is =", y)

x=3
print_Val(x)

x=7
print_Val(x)

x=-9
print_Val(x)
'''
'''
#a=4
#print("sum is ", a+3)
#a=7
#print("sum is ", a+5)
#a=8
#print("sum is ", a+7)

def print_sumA(y):
    print("sum is ", y)
    
a=4
print_sumA(a+3)
a=7
print_sumA(a+5)
a=8
print_sumA(a+7)
'''
'''
#original code
x=int(input())
a=x
a=a+7
print("value of a is ", a)
y=int(input())
a=y+3
a=a+7
print("value of a is ", a)
y=int(input())
print("value of y is ", y)
'''
#new code
def print_a(z):
    z=z+7
    print("value of a is ", z)
x=int(input())
a=x
print_a(a)
y=int(input())
a=y+3
print_a(a)
y=int(input())
print("value of y is ", y)                          