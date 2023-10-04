"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/09/2023
DESCRIPTION : Write a program to print all prime numbers within given range.
SAMPLE IP:  Enter the lower and upper ranges: 900  970 
SAMPLE OP: Prime numbers between 900 and 970 are: 907, 911, 919, 929, 937, 941, 947, 953, 967
"""
a,b=[eval(i) for i in input("Enter the lower and upper ranges : ").split()]
print("Prime numbers between {} and {} are: ".format(a,b),end="")
for i in range(a,b+1):
    if i > 1:  
        for j in range (2, i):  
            if (i % j) == 0:  
                break  
        else:  
            print (i,end=" ")  

