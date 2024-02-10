class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_ele = len(nums)
        min_ele = nums[0]
        for i in range(len(nums)):
            if (nums[i] < min_ele):
                min_ele = nums[i]
        sum_ele = 0
        for i in range(min_ele, max_ele+1):
            sum_ele = sum_ele + i

        for i in range(len(nums)):
            sum_ele = sum_ele - nums[i]
        return sum_ele