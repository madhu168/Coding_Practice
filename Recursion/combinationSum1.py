class Solution:
    def combinationHelper(self, candidates: List[int], target: int, i: int, sum_t: int, ans: List[List[int]], subset: List[int]) -> List[List[int]]:
        if sum_t == target:
            ans.append(subset.copy())
            return
        if i >= len(candidates):
            return
        
        if sum_t > target:
            return
        
        # skip i logic
        self.combinationHelper(candidates,target,i+1,sum_t,ans,subset)

        sum_t += candidates[i]
        subset.append(candidates[i])

        self.combinationHelper(candidates,target,i,sum_t,ans,subset)

        #Backtracking
        sum_t -= candidates[i]
        subset.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sum_track = 0
        subset = []
        ans = []
        self.combinationHelper(candidates,target,0,0,ans,subset)
        return ans