"""NAME : SUGUMAR P
ID : 23012_017
DATE : 29/10/2023
DESCRIPTION :WAP to implement bubble sorting using arrays.
SAMPLE IP:  Enter the elements in array in the form of list- [2,1,5,3]
SAMPLE OP:  Sorted list is: 1 2 3 5
"""
from numpy import *
userList=eval(input())
newarray=array(userList)
arrayLength=len(newarray)
for i in range(arrayLength):
    for j in range(0,arrayLength-i-1):
        if newarray[j]>newarray[j+1]:
            newarray[j],newarray[j+1]=newarray[j+1],newarray[j]
SortedList=newarray.tolist()
print("Sorted list is:",SortedList)