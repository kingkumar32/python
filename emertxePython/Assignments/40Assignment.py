"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : Write a function that capitalizes the first and fourth letters of a name.
SAMPLE IP:  Enter a string: morning
SAMPLE OP:  After capitalising the first and fourth letters of a name: MorNing
"""
def fun(data):
    if len(data)>3:
        newData=[i for i in data]
        newData[0]=newData[0].upper()
        newData[3]=newData[3].upper()
        print("After capitalising the first and fourth letters of a name:","".join(newData))
    else:
        print("After capitalising the first and fourth letters of a name: Name is too short!")


mainString=input()
fun(mainString)

