# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:02:09 2020

@author: craig
"""
'''
#all at once
name = ['tom', 'harry', 'sue', 'todd']
print(name)
name[0], name[3], name[1], name [2] = name[3], name[0], name[2], name[1]
print(name)
'''
'''
#flip pairs
name = ['tom', 'harry', 'sue', 'todd']
print(name)

#flip first and last
temp=name[0]
name[0]=name[3]
name[3]=temp
print(name)

#flip middle two
temp=name[1]
name[1]=name[2]
name[2]=temp
print(name)
'''
'''
#reverse function
name = ['tom', 'harry', 'sue', 'todd']
print(name)
name.reverse()
print(name)
'''
'''
#reversing without hard coding
names=['a','b','c','d','e']
print(names)

size=len(names)
i=0

#exchange a and e
temp=names[0] #stores first item
names[0]=names[size-1]
names[size-1]=temp
print(names)

#exchange b and d
temp=names[1]
names[1]=names[size-2]
names[size-2]=temp
print(names)
'''
#reverse via while loop
names=['a','b','c','d','e']
print(names)

size=len(names)
i=0

while(i<(len(names)/2)):
    temp=names[i]
    names[i]=names[size-(i+1)]
    names[size-(i+1)]=temp
    print(names)
    i=i+1




