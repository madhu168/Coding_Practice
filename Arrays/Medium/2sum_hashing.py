class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        ans_map = {}
        for i in range(len(nums)):
            if nums[i] not in ans_map:
                ans_map[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i] in ans_map) and (i != ans_map[target - nums[i]]):
                ans.append(i)
                ans.append(ans_map[target - nums[i]])
                break
        return ans