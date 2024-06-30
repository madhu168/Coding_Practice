class Solution:
    def subsetHelper(self, nums: list[int], i: int, subSet: list[int], ans: list[list[int]]) -> list[list[int]]:
        #base condition
        if i >= len(nums):
            ans.append(subSet.copy())
            return
        
        #include i
        subSet.append(nums[i])
        self.subsetHelper(nums,i+1,subSet,ans)
        
        #without i
        subSet.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.subsetHelper(nums,i+1,subSet,ans)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subSet = []
        nums.sort()
        self.subsetHelper(nums,0,subSet,ans)
        return ans
        