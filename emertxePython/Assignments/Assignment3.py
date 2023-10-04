""""NAME : SUGUMAR P
ID : 23012_017
DATE : 28/09/2023
DESCRIPTION : WAP to find the greatest of three numbers.
SAMPLE IP:  Enter the first number:  80

            Enter the second number: 10 

            Enter the third number:  20  

SAMPLE OP:   80 is the greatest among the three numbers.
"""

a,b,c=[int(i) for i in input().split()]
result=a if (a>b>c) or (a>c>b) else b if (b>a>c) or (b>c>a) else c
print(result,"is the greatest among the three numbers.")
