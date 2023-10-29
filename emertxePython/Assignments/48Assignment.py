"""NAME : SUGUMAR P
ID : 23012_017
DATE : 29/10/2023
DESCRIPTION :WAP to find all anagrams of a str from a list of strings(using lambda and filter functions).
SAMPLE IP:  Enter the list of strings:['bcda', 'abce', 'cbda', 'cbea', 'adcb']
            Enter string, str: abcd
SAMPLE OP:  Anagrams of 'abcd' in the above string: ['bcda', 'cbda', 'adcb']
"""
userList=eval(input()) #getting list of strings from the user
userString=input()
anagrams=list(filter(lambda a: "".join(sorted(a)) == "".join(sorted(userString.lower())),userList)) #checking for anagrams in the list
print("Anagrams of '{}' in the above string: ".format(userString),anagrams) #prints the list that contains anagrams
