"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/10/2023
DESCRIPTION :WAP to print addition and multiplication of matrix.
SAMPLE IP:  Enter first matrix: [[1,3],[4,6]]
            Enter second matrix: [[1,2],[3,4]]
SAMPLE OP:  [[1 3] 
            [4 6]] 

            Second Matrix: 
            [[1 2] 
            [3 4]] 

            Multiplication of Matrix: 
            [[10 14]                                                                        
            [22 32]] 

            Addition of Matrix:
            [[2 5] 
            [7 10]]
"""

from numpy import *

userMatrix1=array(eval(input())) #importing matrix 1 from the user
userMatrix2=array(eval(input())) #importing matrix 2 from the user

print(userMatrix1)
print(userMatrix2)

print("Multiplication of matrix")
print(matmul(userMatrix1,userMatrix2)) #multiplying two matrix
print("Addition of Matrix")
print(add(userMatrix1,userMatrix2)) # adding two matrix
