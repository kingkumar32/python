f=open("abc.txt","a")
g=f.write("test")
f.close
k=open("abc.txt","r")
l=k.read()
print(l)
k.close
