# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:45:30 2020

@author: craig
"""

#ask the user to enter some numbers
#user will enter "done"

while(True): #infinite loop
    inp = input("Enter the next number >> ")
    
    if(inp == "done"):
        break #stops the loop
    print("you entered ", int(inp))
    
    

    
