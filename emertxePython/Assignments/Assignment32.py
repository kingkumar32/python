"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to print a cube of each element present in the list from the given range from user, using list comprehension.
SAMPLE IP:  1 10
SAMPLE OP:  [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""

startPoint,endPoint=[eval(i) for i in input().split()]
outputLitst=[i**3 for i in range(startPoint,endPoint+1)]
print("Cube of numbers between {} and {} are :".format(startPoint,endPoint),outputLitst)