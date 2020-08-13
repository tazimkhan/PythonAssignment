n=int(input("enter the number"))
'''while(n!=1):
    for e in range(2,n,1):
        if(n%e==0):
            n=int(n/e)
            print(e)
            break
    e=e+1
    if(n==e):
            n=int(n/e)
            print(e)'''

for e in range(2,n+1,1):
    while(n%e==0):
            n=int(n/e)
            print(e)
        
