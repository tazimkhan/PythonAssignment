d={}
l=[]
z=int(input("enter the total numbers of students"))
for e in range(0,z,1):
    s=int(input("enter roll no"))
    l.append(s)
print(l)
print(type(l))
for e in l:
    p=input("enter the name")
    d[e]=p
print(d)
