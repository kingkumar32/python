"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : Write a function that returns lesser of two given numbers if both are even. But it returns greatest if one or both numbers are odd.
SAMPLE IP:  Enter two numbers: 2 4
SAMPLE OP:  Both the given values are even and the smaller of two elements is: 2
"""
numberOne,numberTwo=[int(i) for i in input().split()]
if numberOne%2==0 and numberTwo%2==0:
    if numberOne>numberTwo:
        print("Both the given values are even and the smaller of two elements is:",numberTwo)
    elif numberOne<numberTwo:
        print("Both the given values are even and the smaller of two elements is:",numberOne)
elif numberOne%2!=0 or numberTwo%2!=0:
    if numberOne>numberTwo:
        print("Either one or both the given values are odd and the greater of two elements is:",numberOne)
    elif numberOne<numberTwo:
        print("Either one or both the given values are odd and the greater of two elements is:",numberTwo)

