"""NAME : SUGUMAR P
ID : 23012_017
DATE : 2/10/2023
DESCRIPTION : WAP to separate all alphabets and digits in a given string.
SAMPLE IP:  Enter the String: ab23cg56
SAMPLE OP:  The output after splitting into alphabets and digits: abcg2356
"""
mainString=input()
convertedMainStringToList=list(mainString)
alphabetString=[]
digitString=[]
for i in convertedMainStringToList:
    if i.isalpha():
        alphabetString.append(i)
    elif i.isdigit():
        digitString.append(i)

finalString=alphabetString+digitString
print("The output after splitting into alphabets and digits:","".join(finalString))