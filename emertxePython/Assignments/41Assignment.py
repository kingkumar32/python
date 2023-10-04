"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to reverse the sentence.
SAMPLE IP:  Enter the sentence: I am home
SAMPLE OP:  After reversing the sentence: home am I
"""

def fun(data):
    newlist=[i for i in data.split()]
    newlist.reverse()
    print("After reversing the sentence:"," ".join(newlist))

mainString=input()
fun(mainString)