n=int(input("enter the number"))
z=1
y=2
A=[]
while(z<=n):
    x=2
    while(x<y):
       if(y%x==0 ):
          y+=1
          x=2
          continue
       x=x+1
    else:
        A+=[y]
        z+=1
    y+=1
print(A)
