def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    temp = []
    unique_arr = []
    left = 0
    right = 0
    while(left < len(a) and right < len(b)):
        if(a[left] < b[right]):
            temp.append(a[left])
            left += 1
        elif(a[left] > b[right]):
            temp.append(b[right])
            right += 1
        else:
            temp.append(a[left])
            left += 1
            right += 1
    while(left < len(a)):
        temp.append(a[left])
        left += 1
    while(right < len(b)):
        temp.append(b[right])
        right += 1
    unique_arr.append(temp[0])
    for i in range(1, len(temp)):
        if temp[i] != temp[i - 1]:
            unique_arr.append(temp[i])
    return unique_arr
        
