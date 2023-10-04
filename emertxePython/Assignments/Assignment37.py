"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to delete an element from a particular position in the tuple.
SAMPLE IP:  Enter elements in a tuple: ('a', 'b', 'c', 'd')
            Enter the index value of an element, you want to delete: 1
SAMPLE OP:  New tuple after deleting an existing element:  ('a', 'c', 'd')
"""

mainSequenceTuple=eval(input())
posElement=eval(input())


mainSequenceList=list(mainSequenceTuple)
mainSequenceList.pop(posElement)
mainSequenceTupleNew=tuple(mainSequenceList)
print("New tuple after replaceing an existing element:",mainSequenceTupleNew)