def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    max_length = 0
    preSumMap = {}
    s = 0
    for i in range(len(a)):
        s += a[i]
        if(s == k):
            max_length = max(max_length,i+1)
        rem = s - k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            max_length = max(max_length,length)
        if s not in preSumMap:
            preSumMap[s] = i
    return max_length