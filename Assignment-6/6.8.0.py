n=int(input("enter the number of values"))
A=[]
sum=0
s=0
for e in range(0,n,1):
    ae=int(input("enter the number of values"))
    A+=[ae]
for a in A:
    if(a%2==0):
        sum=sum+a
    else:
        s=s+a
print("sum of even %g"%sum)
print("sum of odd %g"%s)
