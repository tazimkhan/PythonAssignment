s=input("enter the string")
x=input("enter the character")
count=0
for a in s[0::]:
    if(x==a):
        count+=1
print(count)
