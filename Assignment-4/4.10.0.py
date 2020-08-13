n=int(input("enter the number"))
m=int(input("enter the number"))
z= m if m<n else n
for e in range(z,0,-1):
    if(m%e==0 and n%e==0):
        print(e)
        break
