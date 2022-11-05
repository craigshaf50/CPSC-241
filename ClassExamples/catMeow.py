# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:26:09 2020

@author: craig
"""
foundC=0
foundA=0

while(True):
    char=input("Enter the next character or done: ")
    if char=='done':
        break
    if char=='c':
        foundC=1
    elif (char=='a') and (foundC==1):
        foundA=1
    elif (char=='t') and (foundA==1):
        print("MEOW")
    else:
        foundC=0
        foundA=0