class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        ele = None

        for i in range(len(nums)):
            if counter == 0:
                ele = nums[i]
                counter = 1
            elif nums[i] == ele:
                counter += 1
            else:
                counter -= 1

        counter_1 = 0
        for j in range(len(nums)):
            if(nums[j] == ele):
                counter_1 += 1

        if(counter_1 > (len(nums)//2)):
            return ele
        return -1