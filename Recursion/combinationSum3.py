from typing import List

def combinationSumHelper(k: int, target: int, i: int, ans: List[List[int]], subSet: List[int], sumTrack: int) -> List[List[int]]:
    if k == 0:
        if sumTrack == target:
            ans.append(subSet.copy())
        return
    
    if sumTrack > target:
        return
    
    if i > 9:
        return
    
    sumTrack += i
    subSet.append(i)

    combinationSumHelper(k-1,target,i+1,ans,subSet,sumTrack)

    sumTrack -= i
    subSet.pop()

    combinationSumHelper(k,target,i+1,ans,subSet,sumTrack)

def combinationSum(k: int, n: int) -> List[List[int]]:
    ans = []
    subSet = []
    sumTrack = 0
    combinationSumHelper(k,n,1,ans,subSet,sumTrack)
    return ans