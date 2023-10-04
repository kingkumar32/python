""""NAME : SUGUMAR P
ID : 23012_017
DATE : 28/09/2023
DESCRIPTION : Write a program to print the following pattern.
SAMPLE IP:  Enter the number of rows, n=3 

SAMPLE OP:  1
            1 2
            1 2 3 
"""
row=eval(input())

for i in range(row):
    for j in range(row):
        if j<=i:
            print(j+1,end=" ")        
    print()