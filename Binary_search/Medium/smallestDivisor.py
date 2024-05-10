class Solution:
    def threesholdVal(self,nums: List[int],i: int) -> int:
        o_t = 0
        for j in range(len(nums)):
            o_t += math.ceil(nums[j]/i)
        return o_t
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        max_ele = float('-inf')

        for i in range(len(nums)):
            max_ele = max(max_ele,nums[i])
            
        low = 1
        high = max_ele

        while(low <= high):
            mid = (low + high) // 2
            if self.threesholdVal(nums,mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low