d={}
x={}
h=[]
l=[]
z=int(input("enter the total numbers of students"))
for e in range(0,z,1):
    s=input("enter roll no")
    l.append(s)
print(l)
l.sort()
print(l)
for s in l:
    d[s]=input("enter the values")
print(d)
print(type(d))
