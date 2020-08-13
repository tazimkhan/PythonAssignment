n=int(input("enter the number of values"))
A=[]
z=1
for e in range(0,n,1):
    ae=int(input("enter the number of values"))
    A+=[ae]
print(A)
for c in A:
     if(A[0]<c):
        temp=A[0]
        A[0]=c
        c=temp
print(A[0])

