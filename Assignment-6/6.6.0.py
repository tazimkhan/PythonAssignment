n=int(input("enter the number of values"))
A=[]
sum=0
for e in range(0,n,1):
    ae=int(input("enter the number of values"))
    A+=[ae]
m=int(input("enter the occurence element"))
for a in A:
    if(m==a):
        sum+=1
print(A)
print(sum)
