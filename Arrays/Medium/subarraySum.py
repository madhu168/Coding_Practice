from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        preSum = 0
        mpp = defaultdict(int)
        mpp[0] = 1
        for i in range(len(nums)):
            # add current element to prefix Sum:
            preSum += nums[i]
            
            # Calculate x-k:
            remove = preSum - k
            
            # Add the number of subarrays to be removed:
            cnt += mpp[remove]
            
            # Update the count of prefix sum
            # in the map.
            mpp[preSum] += 1
        return cnt