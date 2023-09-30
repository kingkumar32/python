"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/09/2023
DESCRIPTION : WAP to sort the string in alphabetical order.
SAMPLE IP:  Enter the String: Python is easy
SAMPLE OP:  Strings in Sorted Order:  easy is python
"""

mainstring=input().lower()
mainString=mainstring.split()
mainString.sort()
print("Strings in Sorted Order:",' '.join(mainString))