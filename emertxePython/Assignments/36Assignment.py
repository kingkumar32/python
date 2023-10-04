"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to modify or replace an existing item of a tuple with new element.
SAMPLE IP:  Enter elements in a tuple: ('a', 'b', 'c', 'd')
            To replace, enter a new element: 'e'
            Enter the position, you want to replace by new element: 1
SAMPLE OP:  New tuple after replaceing an existing element:  ('a', 'e', 'c', 'd')
"""

mainSequenceTuple=eval(input())
newElement=eval(input())
posElement=eval(input())


mainSequenceList=list(mainSequenceTuple)
mainSequenceList[posElement]=newElement
mainSequenceTupleNew=tuple(mainSequenceList)
print("New tuple after replaceing an existing element:",mainSequenceTupleNew)