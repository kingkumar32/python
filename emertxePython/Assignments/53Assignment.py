"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/10/2023
DESCRIPTION :WAP to print transpose of matrix.
SAMPLE IP:  Enter the elements of the Matrix: [[1,2,3],[4,5,6],[7,8,9]]
SAMPLE OP:  Original Matrix is
            [1, 2, 3]
            [4, 5, 6]
            [7, 8, 9]

            The transpose matrix is: 
            [1, 4, 7]
            [2, 5, 8]
            [3, 6, 9]
"""
from numpy import *

matrixElements=eval(input())

print("Original Matrix is:")
for row in matrixElements:
    print(row)

transposeMatrix=[[matrixElements[j][i] for j in range(len(matrixElements))] for i in range(len(matrixElements[0]))]

print("\nThe transpose matrix is:")
for row in transposeMatrix:
    print(row)
