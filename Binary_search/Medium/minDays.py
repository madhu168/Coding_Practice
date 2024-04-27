class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        val = m * k
        if val > len(bloomDay):
            return -1
        
        min_days = float('inf')
        max_days = float('-inf')
        
        for i in range(len(bloomDay)):
            min_days = min(min_days,bloomDay[i])
            max_days = max(max_days,bloomDay[i])
        
        low = min_days
        high = max_days
        while low <= high:
            mid = (low + high) // 2
            if self.possible(bloomDay,mid,m,k):
                high = mid - 1
            else:
                low = mid + 1
        return low
        
    def possible(self, bloomDay: list[int], day: int, m: int, k: int) -> bool:
        cnt = 0
        noOfB = 0
        
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                cnt += 1
            else:
                noOfB += cnt // k
                cnt = 0
        
        noOfB += cnt // k
        return noOfB >= m
        