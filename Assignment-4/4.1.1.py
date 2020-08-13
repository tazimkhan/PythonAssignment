n=int(input("enter num"))
for e in range(2,n,1):
    if(n%e==0):
        print("num is not prime")
        break
else:
    print("num is prime")
