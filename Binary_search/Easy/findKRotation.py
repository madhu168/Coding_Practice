import sys
def findKRotation(arr : [int]) -> int:
    # Write your code here.
    low = 0
    high = len(arr) - 1
    ans = sys.maxsize
    ans_index = sys.maxsize
    while low <= high:
        mid = (low+high) // 2
        
        if arr[low] <= arr[high]:
            if arr[low] <= ans:
                ans = arr[low]
                ans_index = low
            break
        
        if arr[low] <= arr[mid]:
            if arr[low] <= ans:
                ans = arr[low]
                ans_index = low
            low = mid + 1
        else:
            if arr[mid] <= ans:
                ans = arr[mid]
                ans_index = mid
            high = mid - 1
    return ans_index
