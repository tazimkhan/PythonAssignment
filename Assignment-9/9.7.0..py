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
if(s1.issubset(s)):
    print("s1 is a subset of s")
else:
    print("s1 is a subset of s")
