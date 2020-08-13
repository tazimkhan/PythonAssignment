z=int(input())
for w in range(2,z+1):
    for e in range(2,w,1):
        if w%e==0:
            break
    else:
        if z%w==0:
            print(w)

    
    
