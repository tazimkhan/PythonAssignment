x=input("enter the string")
y=input("enter the string")
z=input("enter the string")
if(x>y and x>z):
    if(y>z):
      print(z,y,x,sep=":")
    else:
      print(y,z,x,sep=":")
elif(y>x and y>z):
    if(x>z):
        print(z,x,y,sep=":")
    else:
        print(x,z,y,sep=":")
elif(z>x and z>y):
    if(x>y):
        print(y,x,z,sep=":")
    else:
        print(x,y,z)
