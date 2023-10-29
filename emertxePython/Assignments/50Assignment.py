"""NAME : SUGUMAR P
ID : 23012_017
DATE : 29/10/2023
DESCRIPTION :Write a program to find total marks and percentage of marks using arrays
SAMPLE IP:  Enter Marks Obtained in 5 Subjects: [46,75,98,34,55]
SAMPLE OP:  Total Mark = 308
            Percentage Mark = 61.6
"""
from numpy import *
a=array(eval(input())) #getting the array value from the user
percentageVal=(sum(a)/(len(a)*100))*100
print("Total Mark =",sum(a)) #print total sum
print("Percentage Mark = ",percentageVal) #printing percentage