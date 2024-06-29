class Solution:
    def subsetHelper(self, nums: list[int], i: int, subSet: list[int], ans: list[list[int]]) -> list[list[int]]:
        #base condition
        if i >= len(nums):
            if subSet not in ans:
                ans.append(subSet.copy())
            return
        
        #include i
        subSet.append(nums[i])
        self.subsetHelper(nums,i+1,subSet,ans)
        
        #without i
        subSet.pop()
        self.subsetHelper(nums,i+1,subSet,ans)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subSet = []
        nums.sort()
        self.subsetHelper(nums,0,subSet,ans)
        return ans
        