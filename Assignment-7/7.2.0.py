s=input("enter the string")
count=0
for w in s[0::]:
    if(w=='a' or w=='i' or w=='e' or w=='o' or w=='u'):
        count+=1
print("the number of vowels %g"%count)
