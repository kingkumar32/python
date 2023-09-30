"""NAME : SUGUMAR P
ID : 23012_017
DATE : 30/09/2023
DESCRIPTION : Write a program to print Fibonacci series upto given number.
SAMPLE IP:  Enter the value of n = 20 
SAMPLE OP: Fibonacci series up to 20 are: 0 1 1 2 3 5 8 13 
"""

number=eval(input("Enter the value of n = "))
k=1
currentnumber=1
previousNumber=0
print("Fibonacci series up to {} are: 0 1 ".format(number),end="")
for i in range(1,number):        
    currentnumber=k
    k=currentnumber+previousNumber
    previousNumber=currentnumber  
    if k>number:
        break      
    print(k,end=" ")
        