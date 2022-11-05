# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:18:29 2020

@author: craig
"""

#lists 10/19
'''
#print items in sequential order

list1=['a', 'b', 'c', 'd', 'e', 'f']
nItems=len(list1) #get number of items in the list

print("number of items = ", nItems, "\n")

i=0 #list index starts at 0

while(i<nItems):
    print("Index - ", i, "Item - ", list1[i])
    i=i+1
 '''   
''' 
#print last item to first item
list1=['a', 'b', 'c', 'd', 'e', 'f']
nItems=len(list1) #get number of items in the list

print("number of items = ", nItems, "\n")
while(nItems>0):
    print("Index - ", nItems-1, "Item - ", list1[nItems-1])
    nItems=nItems-1
'''
'''
list1=['a', 'b', 'c', 'd', 'e', 'f']
for xyz in list1:
    print(xyz)
'''
'''
#Using for loop to access items
list1=['a', 'b', 'c', 'd', 'e', 'f']

i=0
for item in list1:
    print("Index - ", i, "Item - ", item)
    i=i+1
'''
#add five to each item
list1=[1, 2, 3, 4]
nItems=len(list1)
i=0

while(i<nItems):
    list1[i] = list1[i]+5
    i=i+1
print(list1)
