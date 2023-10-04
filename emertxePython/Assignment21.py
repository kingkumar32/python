"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to print the character of a string according to the given number of digit mentioned to the next of it.
SAMPLE IP:   Enter the string, s = a3b4c2e1
SAMPLE OP:  “aaabbbbcce” 
"""
mainString=input("Enter the string, s = ")
characters=[str(i) for i in mainString[0::2]]
numbers=[int(i) for i in (mainString[1::2])]

for i in range(len(numbers)):
    for j in range(numbers[i]):
        print(characters[i],end="")
    

