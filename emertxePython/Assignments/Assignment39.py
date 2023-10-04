"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : Write a function that takes in a two-word string and returns True if both start with same letter, else False.
SAMPLE IP:  Enter the string: animal ant
SAMPLE OP:  True
"""
def startsWithSame(data):
    firstval,secondval=data.split()
    if firstval.startswith(secondval[0]) :
        return True
    else:
        return False
    
mainString=input()
print(startsWithSame(mainString))