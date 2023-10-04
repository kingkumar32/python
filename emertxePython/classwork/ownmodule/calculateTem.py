from tempratureFoumulas import *

data2=eval(input("Enter the celsius : "))
Fahrenheitdata=Fahrenheit(data2)
print("this is in F':",Fahrenheit(data2))
print("this is in c':",celsius(Fahrenheitdata))