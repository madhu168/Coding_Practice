import math
class Solution:
    def findMax(self, v: List[int]) -> int:
        maxi = float('-inf')
        for i in range(len(v)):
            maxi = max(maxi,v[i])
        return maxi

    def calculateTotalHours(self, v: List[int], h: int) -> int:
        totalH = 0
        for i in range(len(v)):
            totalH = totalH + math.ceil(v[i]/h)
        return totalH

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = self.findMax(piles)
        while low <= high:
            mid = (low + high) // 2
            reqTime = self.calculateTotalHours(piles,mid)
            if reqTime <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low