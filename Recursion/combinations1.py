class Solution:
    def combinationsHelper(self, nums: int, ans: List[List[int]], subset: List[int], i: int , k: int) -> List[List[int]]:
        if k == 0:
            ans.append(subset.copy())
            return
        if k > nums - i + 1:
            return
        if i >= nums+1:
            return
        
        subset.append(i)
        self.combinationsHelper(nums,ans,subset,i+1,k-1)
        
        subset.pop()
        self.combinationsHelper(nums,ans,subset,i+1,k)
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        subset = []
        self.combinationsHelper(n, ans, subset,1,k)
        return ans