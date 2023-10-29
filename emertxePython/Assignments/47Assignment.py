"""NAME : SUGUMAR P
ID : 23012_017
DATE : 29/10/2023
DESCRIPTION :WAP to find all palindromes from a list of strings using lambda and filter functions.
SAMPLE IP:  Enter the list of strings: ["geeks", "geeg", "keek", "practice", "aa"]
SAMPLE OP:  List of palindromes: ['geeg', 'keek', 'aa']
"""
userList=eval(input()) #getting list of strings from the user
palindromes=list(filter(lambda a:a == a[::-1],userList)) #checking for palindromes in the list
print("List of palindromes:",palindromes) #prints the list that contains palindromes