"""NAME : SUGUMAR P
ID : 23012_017
DATE : 2/10/2023
DESCRIPTION : WAP to find all positions of a given substring in a main string.
SAMPLE IP:  Enter a String: Python is easy
            Enter substring: is
SAMPLE OP:  Position of a given substring:  7
"""

mainString=input()
subString=input()
beginValue=0
countValue=mainString.count(subString)

if countValue<=1:
    print("Position of a given substring:",mainString.find(subString))
else:
    print("Position of a given substring: ",end="")
    for i in range(countValue):
        d=mainString[beginValue:]
        beginValue=d.find(subString)+beginValue
        print(beginValue,end=" ")
        beginValue+=1





        

