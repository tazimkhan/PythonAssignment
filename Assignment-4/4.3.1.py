z=int(input())
x=2
while z!=0:
    for e in range(2,x,1):
        if x%e==0:
            break
    else:
        print(x)
        z-=1
    x+=1
    
