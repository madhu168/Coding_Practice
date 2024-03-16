class Solution:
    def singleNonDuplicate(self, high: List[int]) -> int:
        n = len(high)
        if n == 1:
            return high[0]
        if high[0] != high[1]:
            return high[0]
        if high[n - 1] != high[n - 2]:
            return high[n - 1]
        low = 1
        high_v = n - 2
        while low <= high_v:
            
            mid = (low+high_v) // 2
            
            if high[mid] != high[mid-1] and high[mid] != high[mid+1]:
                return high[mid]

            if (mid % 2 == 1 and high[mid] == high[mid-1]) or (mid % 2 == 0 and high[mid] == high[mid+1]):
                low = mid + 1
            else:
                high_v = mid - 1

        return -1