"""NAME : SUGUMAR P
ID : 23012_017
DATE : 2/10/2023
DESCRIPTION : WAP to insert a substring in a main string.
SAMPLE IP:  Enter the original string: Flowers beautiful
            Enter the substring to add: are
            Enter specific index value to add the new substring: 8
SAMPLE OP:  The string after inserting substring: Flowers are beautiful
"""
mainString=input()
subString=input()
specificIndex=eval(input())

listedMainString=list(mainString)
listedMainString.insert(specificIndex," ")
listedMainString.insert(specificIndex,subString)
convertedMainString="".join(listedMainString)
print("The string after inserting substring: ",convertedMainString)