n=int(input("enter the number"))
for e in range(0,n+1,1):
    b=e
    count=0
    while(b!=0):
      b=b//10
      count+=1
    sum=0
    a=e
    while(a!=0):
           z=a%10
           sum=sum+z**count
           a=a//10
    if(sum==e):
        print(e)
