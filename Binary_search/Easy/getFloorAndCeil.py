def getFloorAndCeil(a, n, x):
    # Write your code here.
    low = 0
    high = n - 1
    ans_ar = []
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            ans_ar.append(a[mid])
            ans_ar.append(a[mid])
            return ans_ar
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    if high == -1:
        ans_ar.append(-1)
    else:
        ans_ar.append(a[high])
    if low == n:
        ans_ar.append(-1)
    else:
        ans_ar.append(a[low])
    return ans_ar