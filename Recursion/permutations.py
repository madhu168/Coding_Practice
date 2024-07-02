class Solution:
    def permutationsHelper(self, nums: list[int], ans: list[list[int]], pos: int) -> list[list[int]]:
        if pos >= len(nums):
            ans.append(nums.copy())
            return
        
        for i in range(pos,len(nums)):
            nums[i],nums[pos] = nums[pos],nums[i]
            self.permutationsHelper(nums,ans,pos+1)
            nums[i],nums[pos] = nums[pos],nums[i]
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.permutationsHelper(nums,ans,0)
        return ans