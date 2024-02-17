def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    max_length = 0
    for i in range(len(a)):
        for j in range(i,len(a)):
            s = 0
            for l in range(i,j+1):
                s += a[l]
            if(s == k):
                max_length = max(max_length,j+1-i)
    return max_length