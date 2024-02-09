# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def mergeSort(arr,low,high):
    if(low >= high):
        return
    mid = (low+high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp = []
    while(left<= mid and right<=high):
        if(arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while(left <= mid):
        temp.append(arr[left])
        left += 1
    while(right <= high):
        temp.append(arr[right])
        right += 1
    for i in range(low,high+1):
        arr[i] = temp[i-low]

a = [3,4,5,1,2,8,9,7,6]
mergeSort(a,0,len(a)-1)
print(a)