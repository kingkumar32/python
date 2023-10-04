"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to print all even numbers in a given range using normal for loop and list comprehension.
SAMPLE IP:  Enter the start of range: 4
            Enter the end of range: 10
SAMPLE OP:  Even numbers are: [4, 6, 8, 10] 
"""
startVal,endVal=[eval(i) for i in input().split()]
l=[i for i in range(startVal,endVal+1) if i%2==0]
print("Even numbers are:",l)