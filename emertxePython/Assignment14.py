"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/09/2023
DESCRIPTION : WAP to find all positions of a given substring in a main string using find().
SAMPLE IP:  Enter a String: Python is easy
            Enter substring: is
SAMPLE OP:  Position of a given substring:  7
"""
mainString=input()
subString=mainString.split(",")
print("Position of a given substring:",subString[0].find(subString[1]))


