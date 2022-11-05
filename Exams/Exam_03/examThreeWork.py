# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:43:00 2020

@author: craig
"""
'''
list1=[1,3,5,2,1]
list2=[8,2,1,3,4]


def compareList(a,b):
    sum=0
    for item in a:
        sum=sum+item
    print("Sum is ", sum)
    prod=1
    for item in b:
        prod=prod*item
    print("Product is ", prod)
    if (sum<prod):
        return True
    else:
        return False

comparison=compareList(list1, list2)      

print(comparison)
'''
'''
integerList=[1,3,3,4,5,6,7,2,8,3,2,9,0]
K=int(input("Enter value for K >> "))

def sumList(list1,kVal):
    if(kVal<0):
        return integerList==[]
    else:
        sum=0
        i=0
        while i<=kVal-1:
            sum=sum+list1[i]
            i=i+1
            print(sum)
        return sum

print("The sum from index 0 to index ", K-1," is ", sumList(integerList, K))
'''
'''
integerList=[55,2,112,237,80,12,75,20,89,67,69,31,1,3,4,23,99]

def checkFor_99(list1):
    i=0
    found=0
    while(i<len(list1)):
        if(list1[i]==99):
            found=1
        i=i+1
    if(found != 0):
        return True
    else:
        return False
    
print(checkFor_99(integerList))
        
'''

userString=input("Enter a string with even number of characters >> ")

listOfChar=list(userString)

firstHalf=[]
secondHalf=[]

i=0
while(i<(len(listOfChar))/2):
    firstHalf.append(listOfChar[i])
    i=i+1
while(i<len(listOfChar)):
    secondHalf.append(listOfChar[i])
    i=i+1

if(firstHalf==secondHalf):
    print("The string is a twin")
else:
    print("the string is not a twin")
    
















































