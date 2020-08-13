n=int(input("enter the number of values"))
A=[]
s=[]
z=1
for e in range(0,n,1):
    ae=int(input("enter the number of values"))
    A+=[ae]
print(A)
for e in A:
    x=A.count(e)
    if(s.count(e)<1):
        s=s+[e]
        print(e,x)
    else:
        pass
