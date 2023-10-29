"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/10/2023
DESCRIPTION : WAP to accept two matrices and find their product. (read the matrices from the user) using numpy.
SAMPLE IP:  Enter elements of 1st matrix: [[12,45,34],[23,45,23],[56,44,3]]         
            Enter elements of 2nd matrix: [[2,1,7],[4,5,4],[6,98,78]]
SAMPLE OP:  Product of two matrices: 
        [[408 3569 2916]
        [364 2502 2135]
        [306 570 802]]
"""
from numpy import *

userMatrix1=array(eval(input())) #importing matrix 1 from the user
userMatrix2=array(eval(input())) #importing matrix 2 from the user
print("Sum of two matrices:")
print(matmul(userMatrix1,userMatrix2)) # multiplying two matrix