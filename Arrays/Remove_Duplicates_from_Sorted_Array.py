class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        max_element = nums[0]
        max_index = 0
        counter = 1
        for i in range(len(nums)):
            if(nums[i] > max_element):
                max_index += 1
                max_element = nums[i]
                nums[max_index],nums[i] = nums[i],nums[max_index]
                counter += 1
        return counter