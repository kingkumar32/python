"""NAME : SUGUMAR P
ID : 23012_017
DATE : 2/10/2023
DESCRIPTION : WAP to count the number of occurrences of a substring from main string.
SAMPLE IP:  Enter the string: This academy is the best academy
            Enter the substring to count: academy
SAMPLE OP:  Number of times substring occurs in the given string:  2
"""
mainString,subString=[i for i in input().split(",")]
print("Number of times substring occurs in the given string: ",mainString.count(subString))