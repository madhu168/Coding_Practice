arr = [13,46,24,52,20,9]
for i in range(len(arr)):
    j = i
    while(j>0 and arr[j-1] > arr[j]):
        arr[j-1],arr[j] = arr[j],arr[j-1]
        j -= 1
print(arr)