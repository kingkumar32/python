"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/10/2023
DESCRIPTION :WAP to find sum, average of elements in 2D array.
SAMPLE IP:  [[1,2],[3,4]]
SAMPLE OP:  Sum of elements in 2D array= 10
            Average of 2D array=2.5
"""
from numpy import *

userArray = array(eval(input()))
flatarray=userArray.flatten() #we are flatting the array 
print("Sum of elements in 2D array=",sum(flatarray)) #sum of elements in the array
print("Average of 2D array=",sum(flatarray)/size(flatarray)) #average of elements in the array