"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to print only first characters in each strings from a list of strings. (using list comprehension)
SAMPLE IP:  Enter elements in the list: Orange Apple Banana
SAMPLE OP:  City names greater than or equal to 5 are:  ['O', 'A', 'B']
"""

newList=eval(input())
newCityList=[i[0] for i in newList]
print("First character of cities are:",newCityList)