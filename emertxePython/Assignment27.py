"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to count the number of occurrence of element in the list.
SAMPLE IP:  How many elements in list, please enter number:- 7
            Enter elements: 6 7 6 1 0 6 3
            n: 6
SAMPLE OP:  Number of occurrence of 6 is 3.
"""

mainList=eval(input())
n=eval(input())

print("Number of occurrence of",n,"is",mainList.count(n))