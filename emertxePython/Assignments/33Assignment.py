"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to print the sum and average of the elements present in the tuple.(using built-in functions and without using them)
SAMPLE IP:  Enter the elements into the tuple: (1,1,1,1)
SAMPLE OP:  The summation of tuple elements is: 4
            The Average of tuple elements is: 1
"""
mainSequenceTuple=(eval(input()))
mainSequenceList=list(mainSequenceTuple)
sumOfElements=sum(mainSequenceList)
averageOfElements=(sumOfElements/len(mainSequenceList))
print("The summation of tuple elements is:",sumOfElements)
print("The Average of tuple elements is:",averageOfElements)

'''
sumOfElementsTwo=0
for i in mainSequenceList:
    sumOfElementsTwo=sumOfElementsTwo+i

print("The summation of tuple elements is:",sumOfElementsTwo)
'''
