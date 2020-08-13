n=int(input("enter num"))
z=2
while(z<n):
    if(n%z==0):
        print("num is not prime")
        break
    z+=1
else:
    print("num is prime")
