n=int(input("enter num"))
for e in range(n+1,2*n,1):
    for num in range(2,e):
        if(e%num==0):
            break
    else:
        print(e)
        break
    
