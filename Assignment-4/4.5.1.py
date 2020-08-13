n=int(input("enter the number"))
m=int(input("enter the number"))
if(n<m):
    z=n
else:
    z=m
while(z>1):
    if(n%z==0 and m%z==0):
        print("number r not co-prime")
        break
    z-=1
else:
    print("number r co-prime")
