n=int(input("enter the number"))
m=int(input("enter the number"))
z=n+1
while(z<m):
    x=2
    while(x<z):
        if(z%x==0):
            break
        x+=1
    else:
        print(z)
    z+=1
