class Solution:
    def permutationsHelper(self, nums: list[int], ans: List[List[int]], pos: int) -> List[List[int]]:
        if pos >= len(nums):
            ans.append(nums.copy())
            return
        track = set()
        for i in range(pos, len(nums)):
            if nums[i] in track:
                continue
            track.add(nums[i])
            nums[i],nums[pos] = nums[pos],nums[i]
            self.permutationsHelper(nums,ans,pos+1)
            nums[i],nums[pos] = nums[pos],nums[i]
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.permutationsHelper(nums,ans,0)
        return ans