"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to insert a new item into a tuple at a specified location.
SAMPLE IP:  Enter elements in a tuple: ('a', 'b', 'c', 'd')
            To insert, enter a new element: 'e'
            Enter the position, you want to insert new element: 4
SAMPLE OP:  New tuple after adding a new element:  ('a', 'b', 'c', 'd', 'e')
"""
mainSequenceTuple=eval(input())
newElement=eval(input())
posElement=eval(input())


mainSequenceList=list(mainSequenceTuple)
mainSequenceList.insert(posElement,newElement)
mainSequenceTupleNew=tuple(mainSequenceList)
print("New tuple after adding a new element:",mainSequenceTupleNew)