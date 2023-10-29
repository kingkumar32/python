"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/10/2023
DESCRIPTION : WAP to accept two matrices and find their sum using numpy.(read the matrices from the user)
SAMPLE IP:  Enter elements of 1st matrix:[[2,3,4],[5,2,3]]
            Enter elements of 2nd matrix:[[-4,5,3],[5,6,3]]
SAMPLE OP:  Sum of two matrices: 
          [[-2   8   7]   
          [10   8    6]]
"""

from numpy import *

userMatrix1=array(eval(input())) #importing matrix 1 from the user
userMatrix2=array(eval(input())) #importing matrix 2 from the user
print("Sum of two matrices:")
print(add(userMatrix1,userMatrix2)) # adding two matrix