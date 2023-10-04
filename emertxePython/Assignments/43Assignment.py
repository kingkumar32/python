"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : Write a function that takes in a list of integers and returns True if it contains 007 in order.
SAMPLE IP:  Enter the list: [1,2,9,0,0,7,2,3]
SAMPLE OP:  True
"""
def fun(data):
    testList=[0,0,7]
    countVal=0
    jumpPos=0    
    itervalue=0
    for j in range(len(testList)):
        for i in data[jumpPos::]:            
            itervalue+=1           
            if i==testList[j]:
                jumpPos=itervalue
                countVal+=1
                break            
            
    if countVal==3:
        return True
    else:
        return False    

mainString=eval(input())
print(fun(mainString))