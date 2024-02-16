class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1s = 0
        count = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                count = count + 1
            else:
                count = 0
            if(count > max_1s):
                max_1s = count

        return max_1s