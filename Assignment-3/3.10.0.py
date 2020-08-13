n=int(input("enter num"))
z=1
pro=1
while(z<=2*n):
    if(z%2!=0):
        pro=pro*z
    z+=1
print(pro)
