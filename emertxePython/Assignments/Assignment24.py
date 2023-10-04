"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to merge two strings alternatively.
SAMPLE IP:  Enter the string, S1: ABC
            Enter the string, S2: DEF
SAMPLE OP:   The merged string: ADBECF
"""
stringOne,stringTwo=[i for i in input("").split()]
newString=[]
totalLength=len(stringOne)+len(stringTwo)

for i in range(int(totalLength)):
    if i<len(stringOne):
        newString.append(stringOne[i])
    if i<len(stringTwo):
        newString.append(stringTwo[i])

print("The merged string:","".join(newString))