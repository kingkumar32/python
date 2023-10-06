from array import array
a=array('i',[1,2,3,4,5])
c=a
b=array(a.typecode,(i for i in a)) #copying an array

print(a is b)
print(c is a)
