"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to implement bubble sorting.
SAMPLE IP:  Enter the elements into the list: [4,3,1,5,2]
SAMPLE OP:  Sorted list is: 1 2 3 5
"""

mainList=eval(input())

for i in range(len(mainList)):
    for j in range(0,len(mainList)-1-i):
        if mainList[j]>mainList[j+1]:
            temp=mainList[j]       
            mainList[j]=mainList[j+1]   
            mainList[j+1]=temp             
              
print("Sorted list is:",mainList)