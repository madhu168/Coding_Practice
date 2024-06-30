class Solution:
    def combinationSumHelper(self, candidates: List[int], target: int, i: int, sumTrack: int, subSet: List[int], ans: List[List[int]]) -> List[List[int]]:
        if sumTrack == target:
            ans.append(subSet.copy())
            return
        if i >= len(candidates):
            return
        if sumTrack > target:
            return

        sumTrack += candidates[i]
        subSet.append(candidates[i])
        self.combinationSumHelper(candidates,target,i+1, sumTrack,subSet,ans)

        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1

        sumTrack -= candidates[i]
        subSet.pop()
        self.combinationSumHelper(candidates,target,i+1,sumTrack,subSet,ans)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subSet = []
        sumTrack = 0
        candidates.sort()
        self.combinationSumHelper(candidates,target,0,sumTrack,subSet,ans)
        return ans
        