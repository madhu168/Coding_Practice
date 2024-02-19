class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        f = []
        for i in range(len(nums)):
            if nums[i] > 0:
                p.append(nums[i])
            if nums[i] < 0:
                n.append(nums[i])

        for x,y in zip(p,n):
            f.append(x)
            f.append(y)
        return f