# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:33:53 2020

@author: craig
"""


sum=0


while(True):
    numVal = input("enter the number or done >> ")
    if(numVal == "done"):
        print("sum is: ", sum)
        break
    sum = sum + int(numVal)
    