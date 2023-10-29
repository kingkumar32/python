"""NAME : SUGUMAR P
ID : 23012_017
DATE : 29/10/2023
DESCRIPTION :WAP to print message when user passes their name by using decorators.
SAMPLE IP:  Enter string: Rohan
            Enter your name: Rohan
SAMPLE OP:  hello Rohan How are you?
"""
def greeting(str):
    def checkval():
        data=str()
        if data== userName:
            return print("hello",data,"How are you?")
        else:
            return print("hello,",userName,"good morning!")        
    return checkval         

userString,userName=input().split()


def str():
    return userString

res=greeting(str)
res()



