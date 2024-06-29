class Solution:
    def subsetHelper(self, nums: list[int], i: int, subSet: list[int], ans: list[list[int]]) -> list[list[int]]:
        #base condition
        if i >= len(nums):
            if subSet.copy not in ans:
                ans.append(subSet.copy())
            return
        
        #include i
        subSet.append(nums[i])
        self.subsetHelper(nums,i+1,subSet,ans)
        
        #without i
        subSet.pop()
        self.subsetHelper(nums,i+1,subSet,ans)
        
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        subSet = []
        self.subsetHelper(nums,0,subSet,ans)
        return ans