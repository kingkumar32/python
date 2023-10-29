"""NAME : SUGUMAR P
ID : 23012_017
DATE : 29/10/2023
DESCRIPTION :Find out maximum and minimum number from a list using lambda and reduce functions.
SAMPLE IP:  Enter List: [2, 1, 5, 3]
SAMPLE OP:  The minimum number in a list: 1
            The maximum number in a list: 5
"""

from functools import *
l=eval(input()) #getting the list of values from the user
minVal=reduce((lambda x,y:x if x < y else y),l) #checking for the minimum value
maxVal=reduce((lambda x,y:x if x > y else y),l) #checking for the maximum value 
print("The minimum number in a list:",minVal)
print("The maximum number in a list:",maxVal)