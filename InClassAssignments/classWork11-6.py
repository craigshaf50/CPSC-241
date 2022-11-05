# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:05:32 2020

@author: craig
"""
'''
word_list = ['he', 'll', 'o', ' ', 'to', 'm']
print(word_list[0:len(word_list):2])
'''
'''
word_list.remove('m')
word_list.remove('to')
print(word_list)

word_list.append('ma')
word_list.append('tt')
print(word_list)
'''

'''
word1=['my', 'dog']
word2=['is', 'nice']

word3=word1+word2
print(word3)
'''
'''
animals=['r','h','i','n','o','s']
i=len(animals)//2 - 1
while(i > -1):
    print(animals[i])
    i=i-1
'''
myarray=[0,1,1,0,0,1,1]
i=0
totalOnes=0
while (i<len(myarray)):
    if myarray[i]==1:
        totalOnes=totalOnes+1
    i=i+1        
print("there are ", totalOnes, "ones in myarray")
        






