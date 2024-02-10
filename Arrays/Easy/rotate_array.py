class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(k > len(nums)):
            k = k % len(nums)
        first_half = nums[:len(nums)-k]
        second_half = nums[len(nums)-k:]
        combined_list = second_half + first_half
        for i in range(len(combined_list)):
            nums[i] = combined_list[i]