####################################################
#
# author: Craig Shaffer
# date revision: 9/4/20
# course: CPSC 241
#
# code to compute the area of the rectangle
#
# input - length and width
# output - area of a rectangle
#
####################################################

print("compute the area of a rectangle")

#enter the length - integer
length=input("enter the length of the rectangle >> ")
length=int(length)

#enter the width - integer
width=input("enter the width of the rectangle >> ")
width=int(width)

#compute area
area = length*width

#print message and the value of the rectangle's area
print("area of the rectangle is >> ", area)
