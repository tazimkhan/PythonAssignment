n=int(input("enter the number of values"))
A=[]
sum=0
for e in range(0,n,1):
    ae=int(input("enter the number of values"))
    A+=[ae]
print(A)
for e in A:
    sum=sum+e
print(sum)
