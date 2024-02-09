# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def quickSort(arr,low,high):
    if(low < high):
        pIndex = partition(arr,low,high)
        quickSort(arr,low,pIndex-1)
        quickSort(arr,pIndex+1,high)

def partition(arr,low,high):
    i = low
    j = high
    pivot = arr[low]
    while(i<j):
        while(arr[i] <= pivot and i <= high-1):
            i += 1
        while(arr[j] > pivot and j >= low-1):
            j -= 1
        if(i < j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j

a = [3,4,5,1,2,8,9,7,6]
quickSort(a,0,len(a)-1)
print(a)