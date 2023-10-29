"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/10/2023
DESCRIPTION :WAP to retrieve biggest item after comparing 2 arrays using where() method.
SAMPLE IP:  Enter 1st array: [2, 15, 5, 3]
            Enter 2nd array: [9,3,20,23]
SAMPLE OP:  The list of maximum values: [9,15,20,23]
"""
from numpy import *

userArray1=array(eval(input())) #getting array one values
userArray2=array(eval(input())) #getting array two values

maxValInArray=where(userArray1>userArray2,userArray1,userArray2) #getting the biggest item in array

print("The list of maximum values:",maxValInArray) #printing max values