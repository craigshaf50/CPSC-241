# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:03:57 2020

@author: craig
"""
'''
#shortcut to remove duplicates
def remove_duplicates(list):
    listNew=[]
    
    for item in list:
        if(not(item in listNew)):
            listNew.append(item)
            
    print(listNew)

listOld=[5,1,2,5,1,2,3,3,4]

remove_duplicates(listOld)
'''
#check if key is in a list manually

def check_key(list, key):
    for item in list:
        if(item==key):
            print("item found")
            break

list1=[23,56,21,-9,67,12]
key1=12

check_key(list1,key1)

