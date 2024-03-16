def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here
    low = 0
    high = len(arr) - 1
    ans_ar = []
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    last = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    if first == -1:
        return 0
    else:
        return last - first + 1
