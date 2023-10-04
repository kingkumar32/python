"""NAME : SUGUMAR P
ID : 23012_017
DATE : 28/09/2023
DESCRIPTION : Write a program to print odd numbers in a given range m to n
SAMPLE IP:  Enter the starting value(m) = 7 

            Enter the end value(n) = 13 
SAMPLE OP: Odd numbers between 7 and 13 are: 7,9, 11, 13 
"""
m,n=[eval(i) for i in input().split()]
print("Odd numbers between",m,"and",n,"are: ",end="")
for i in range(m,n+1):
    if i%2:
        print(i,end=" ")