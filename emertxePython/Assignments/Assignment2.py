""""NAME : SUGUMAR P
ID : 23012_017
DATE : 28/09/2023
DESCRIPTION : Write a program to check whether the number entered by the user is even or odd.
SAMPLE IP:   Input: Enter the number: 43           
SAMPLE OP:  Output: 43 is a positive odd number.
"""

a=eval(input("Enter the number : "))
if a%2:
    if a>0:
        print(a,"is a positive odd number")
    else :
        print(a,"is a negative odd number")
elif a==0:
    print("0 is neither odd nor even")
else :
    if a>0:
        print(a,"is a positive even number")
    else :
        print(a,"is a negative even number")