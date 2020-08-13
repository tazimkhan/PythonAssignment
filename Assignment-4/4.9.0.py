n=int(input("enter the number"))
m=int(input("enter the number"))
z= m if m>n else n
for e in range(z,(m*n+1),1):
    if(e%m==0 and e%n==0):
        print(e)
        break
