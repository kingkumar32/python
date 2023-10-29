"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/10/2023
DESCRIPTION :WAP for Linear Search.
SAMPLE IP:  Enter List: [2, 4, 0, 1, 9]
            Enter the element to search: 9
SAMPLE OP:  Element found at index: 4
"""
from numpy import *
def linSearch(newarray,searchElement):
    for i,element in enumerate(newarray):
        if element == searchElement:
            return i
    return -1


newarray=array(eval(input())) #getting the array as list from the user
searchElement=eval(input()) #getting the search element
result = linSearch(newarray,searchElement) #we are calling the function to search

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")

