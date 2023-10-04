""""NAME : SUGUMAR P
ID : 23012_017
DATE : 28/09/2023
DESCRIPTION : Write a program to print the following pattern.
SAMPLE IP:  Enter the number of rows, n=3 

SAMPLE OP:  2
            2 4
            2 4 8 
"""
row=eval(input())
val=1
for i in range(1,row+1):
    for j in range(1,row+1):
        if j<=i:
            val=val+val
            print(val,end=" ")   
    val=1     
    print()