d={}
s=set()
z=int(input("enter the number of keys"))
for e in range(0,z,1):
    a=input("enter the keys values")
    s.add(a)
print(s)
for w in s:
    f=input("the value of dict")
    d[w]=f
print(d)
for q in d:
    print("key=",q,"value=",d[q])

