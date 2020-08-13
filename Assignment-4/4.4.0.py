n=int(input("enter the number"))
m=int(input("enter the number"))
for e in range(n+1,m,1):
    for num in range(2,e,1):
        if(e%num==0):
            break
    else:
        print(e)
