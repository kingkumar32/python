""""NAME : SUGUMAR P
ID : 23012_017
DATE : 26/09/2023
DESCRIPTION : Write a single line code to take 3 values from the user. All three should belong to different data types.
SAMPLE IP:  Enter 3 values : 1   2.3   4+5j            
SAMPLE OP:  The values are :

                   1 belongs to <class 'int'>

                   2.3 belongs to <class 'float'>

                   4+5j belongs to <class 'complex'
"""

a,b,c=[eval(i) for i in (input()).split()]
print("The values are : ")
print(a," belongs to ",type(a))
print(b," belongs to ",type(b))
print(c," belongs to ",type(c))