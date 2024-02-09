a = [8,7,6,3,4,5,1,2,9,0]
for i in range(len(a)):
    mini = i
    for j in range(i+1,len(a)):
        if(a[mini] > a[j]):
            mini = j
    a[i],a[mini] = a[mini],a[i]
print(a)