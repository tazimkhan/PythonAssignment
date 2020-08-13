s1=float(input("emter the marks"))
s2=float(input("emter the marks"))
s3=float(input("emter the marks"))
s4=float(input("emter the marks"))
s5=float(input("emter the marks"))
sum=s1+s2+s3+s4+s5
if(sum>=150):
    print("Pass")
else:
    print("fail")
avg=sum/5
print(avg)
if(avg>=75 and avg<=100):
    print("1st")
elif(avg>=60 and avg<75):
    print("2nd")
elif(avg>=30 and avg<60):
    print("3rd")
