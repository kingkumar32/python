import re

# l=re.subn("\d","#","cy3gh3cg23cr6qg")
# k=re.split("\d","cy3gh3cg23cr6qg")
# g=re.findall(r"Hello$","worldHello")

s="ard:9786543298 123456789945 87654321 8888666643 2345678912"
l=re.findall(r"[9876]\d{9}",s)
print(l)



# d=re.findall("^9",k)
# print(l)
# print(k)
# print(g)
# print(d)

    