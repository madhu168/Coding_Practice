import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_s = -sys.maxsize-1
        for i in range(len(nums)):
            s += nums[i]
            if s > max_s:
                max_s = s
            if s < 0:
                s = 0
        return max_s