# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:14:05 2020

@author: craig
"""
'''
list1=[0,1,2,3]

i=0 #index

for num in list1:
    num=num+5
    list1[i]=num
    i=i+1
print(list1)
'''
'''
list2=[] #empty list
i=0
N=int(input("enter number of items >> "))
while(i<N):
    list2.append(i)
    i=i+1
    print(list2)
'''
'''
list1=[1,3,5,6]
list2=[0,2,4,5]
list3=[]
i=0

while(i<len(list1)):
    temp=list1[i]+list2[i]
    list3.append(temp)
    i=i+1
    print(list3)
'''
list1=[12,34,-5,6,7,99,100]

key=int(input("ENTER KEY >> "))
'''
listSize=len(list1)
found=0
i=0

while(i<listSize):
    if(list1[i]==key):
        print("match ", i)
        found=1
    i=i+1
    
if found==0:
    print("key is not found")
'''
i=0
for myitem in list1:
    if (myitem==key):
        print("index - ", i)
    i=i+1
