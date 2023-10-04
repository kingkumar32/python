"""NAME : SUGUMAR P
ID : 23012_017
DATE : 4/10/2023
DESCRIPTION : WAP to take a list of city names and print those city names in upper cases whose length is greater than or equal to 5.
SAMPLE IP:  Enter city names in the list: ["Pune","Mumbai","Bengaluru"]
SAMPLE OP:  City names greater than or equal to 5 are:  ['MUMBAI', 'BENGALURU']
"""
cityNameList=eval(input())
newCityNameList=[]
for i in cityNameList:
    if len(i)>4:
        j=i.upper()
        newCityNameList.append(j)
print("City names greater than or equal to 5 are:",newCityNameList)