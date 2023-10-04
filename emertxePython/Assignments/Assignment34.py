"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to find the first occurrence of an element in a tuple.
SAMPLE IP:  Enter the elements in the tuple and then enter the element to find the first occurrence: ('a', 'i', 'e', 'k', 'i')  i
SAMPLE OP:  The first occurrence of an element in a tuple: 1
"""

mainSequenceTuple,findElement=[i for i in input().split()]
mainSequenceTuple=eval(mainSequenceTuple)
print("The first occurrence of an element in a tuple:",mainSequenceTuple.index(findElement))