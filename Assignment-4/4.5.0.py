n=int(input("enter the number"))
m=int(input("enter the number"))
if(n<m):
    z=n
else:
    z=m
for e in range(z,1,-1):
    if(n%z==0 and m%z==0):
        print("number r not co-prime")
        break
else:
    print("number are co-prime")

