a = [8,7,6,3,4,5,1,2,9,0,-1]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[j] < a[i]):
            a[i],a[j] = a[j],a[i]
print(a)