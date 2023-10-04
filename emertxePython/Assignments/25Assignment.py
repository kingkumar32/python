"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to Find the minimum and maximum number in a list. (using built-in functions and without using them).
SAMPLE IP:  Enter the elements into the list: 4 3 1 5 2
SAMPLE OP:  The minimum number in a list: 1
            The maximum number in a list: 5
"""
mainList=eval(input())
print("The minimum number in a list: ",min(mainList))
print("The maximum number in a list: ",max(mainList))

'''maxValue=mainList[0]
minValue=mainList[0]
for i in mainList:
    if maxValue<=i:
        maxValue=i
    if minValue>=i:
        minValue=i
print("The minimum number in a list: ",minValue)
print("The maximum number in a list: ",maxValue)'''