d={}
l=[]
sum=0
z=int(input("enter the total numbers of students"))
for e in range(0,z,1):
    s=input("enter roll no")
    l.append(s)
print(l)
l.sort()
print(l)
for s in l:
    d[s]=int(input("enter the values"))
    sum=sum+d[s]
print(d)
print(sum)
