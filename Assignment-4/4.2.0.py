n=int(input("enter num"))
z=n+1
while(z<2*n):
    x=2
    while(x<z):
        if(z%x==0):
            break
        x+=1
    else:
        print(z)
        break
    z+=1
        
