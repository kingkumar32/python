"""NAME : SUGUMAR P
ID : 23012_017
DATE : 2/10/2023
DESCRIPTION : WAP to separate all alphabets and digits in a given string and after separating alphabets and digits, sort both.
SAMPLE IP:   Enter the String: 56casd78
SAMPLE OP:  The output after sorting: acds5678
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
alphabetString.sort()
digitString.sort()
finalString=alphabetString+digitString
print("The output after sorting:","".join(finalString))