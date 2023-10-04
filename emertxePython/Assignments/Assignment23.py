"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to reverse each word of a string individually.
SAMPLE IP:   Enter the String: hi hello how are you
SAMPLE OP:   After reversing each word from the sentence: ih olleh woh era uoy 
"""
mainList=[i for i in input().split()]
for i in range(len(mainList)):
    sublist=list(mainList[i])
    sublist.reverse()
    resublist="".join(sublist)
    mainList[i]=resublist

print("After reversing each word from the sentence:"," ".join(mainList))