"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to reverse the words of a string.
SAMPLE IP:   Enter the String: hi hello how are you
SAMPLE OP:  After reversing:  you are how hello hi 
"""

mainList=[i for i in input().split()]
mainList.reverse()
print("After reversing:"," ".join(mainList))