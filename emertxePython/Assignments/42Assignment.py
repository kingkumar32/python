"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : Write a function that counts number of times the given pattern appears in a string.
SAMPLE IP:  Enter the strings seperated by space: hahaababnaab ab 
SAMPLE OP:  The number of times the given pattern appears in a string: 3
"""

def fun(data):
    newlist,searchString=[i for i in data.split()]
    newlist.count(searchString)
    print("The number of times the given pattern appears in a string:",newlist.count(searchString))

mainString=input()
fun(mainString)