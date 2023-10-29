"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/10/2023
DESCRIPTION :WAP to sort the Matrix row wise using numpy array.
SAMPLE IP:  Enter the elements into the matrix: [[2,6,5],[1,9,8],[7,3,10]]
SAMPLE OP:  Input Matrix:
            [[2 6 5] 
            [1 9 8]
            [7 3 10]] 
            Input Matrix after sorting row and column-wise:
            [[1 9 8] 
            [2 6 5]
            [7 3 10]] 
"""
from numpy import *
userMatrix=array(eval(input())) #get user matrix
print("Input Matrix:")
print(userMatrix)
indexes=argsort(userMatrix[:,0])
sortedMatrix= userMatrix[indexes] #sorting only row 
print("Input Matrix after sorting row ")
print(sortedMatrix) #printing the sorted matrix
