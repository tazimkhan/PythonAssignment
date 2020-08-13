s=input("enter the string")
x=s.split(' ')
y=0
temp=0
while(y<len(x)):
    for e in range(0,len(x)-1,1):
        if(x[e]<x[e+1]):
            temp=x[e]
            x[e]=x[e+1]
            x[e+1]=x[e]
print(x)
















'''for e in x:
    for a in x:
        if(y==0):
            y+=1
        else:
            if(e>a):
                continue
            else:
                temp=e
                e=a
                a=temp
print(x)'''
