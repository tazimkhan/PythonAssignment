x=float(input("enter the the value"))
if(x<=0 or x>=13):
    print("enter the right month value")
elif(x>0 and x<=7):
    if(x%2==0):
        print(30)
    else:
        print(31)
else:
    if(x%2==0):
        print(31)
    else:
        print(30)
