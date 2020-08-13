s=set()
z=int(input("enter the number of keys"))
for e in range(0,z,1):
    a=input("enter the keys values")
    s.add(a)
print(s)
s1=set()
x=int(input("enter the number of keys"))
for e in range(0,x,1):
    a=input("enter the keys values")
    s1.add(a)
print(s1)
print("common element",s1.union(s))
